"""
This module provides several well-known sequences related to Collatz sequences.

Unless explicitely mentioned, all sequences provided here implement the [iterator protocol](https://docs.python.org/3/library/stdtypes.html#iterator-types). That is, they can be used in `for` loops, and as parameter for the built-in `iter()` and `next()` functions. It also means that only one item is kept in memory at a time, the next items being generated on demand or lazily. Unlike container types like lists or dictionnaries, data are not stored but forgotten once the next item is yield. By the way, iterators are very memory-efficient and can process infinite data streams, like most of the sequences generated here.

The available sequences are the following:

| sequence | [OEIS](https://oeis.org/) reference | Description |
| -------- | ----------------------------------- | ----------- |
| total_stopping_time_records | A006877 | Sequence of starting values of Collatz sequences with a total stopping time longer than of any smaller starting value. |
| max_value_records | A006884 | Sequence of starting values of Collatz sequences with maximum values higher than of any smaller starting value. |


"""

from collections import namedtuple
from collections.abc import Iterator
from itertools import count

from gmpy2 import bit_scan1

Record = namedtuple("Record", "rank value")

class total_stopping_time_records(Iterator):
	"""
	Sequence of starting values of Collatz sequences with a total stopping time longer than of any smaller starting value. OEIS reference: [A006877](https://oeis.org/A006877).
	
	!!! example
		
		6 is included in this sequence because the total stopping time of the Collatz sequence beginning by 6 (that is, 8) is greater than total stopping times of all Collatz sequences beginning by 1, 2, 3, 4 and 5.
	
	In order to speedup the computation, it is possible to apply optional optimizations. Those optimizations are combinable (by addition of their numbers) for a greater efficiency. Deeper details (including mathematical demontrations) are available in [this article from T. Leavens and M. Vermeulen](https://oeis.org/A006877/a006877_1.pdf).
	
	The available sorts of optimizations are the following (the speedup factor is calculated with the first 50 records. It is only indicative, since it may differ on your own configuration):
	
	| Number | Name | Description | Speedup factor |
	| ------ | ---- | ----------- | -------------- |
	| 0      | None | No optimization | 1.0 |
	| 1      | Even numbers | Due to the fact that `Syracuse(2k).total_stopping_time` = `Syracuse(k).total_stopping_time + 1`, it is easy to predict the next even candidate for this sequence, and then it is not necessary to compute the Collatz sequences for the other even numbers below this candidate. | 1.9 |
	| 2      | k mod 6 = 5 | If the remainder of the division of the initial value by 6 is 5, then this cannot be a record for the total stopping time. | 1.2 |
	| 4      | *a posteriori* cutoff | It is possible to stop the iteration process of a Collatz sequence before its end, by comparing the current iterate value with all previous records and the number of steps necessary to reach it. **This optimization needs to store all items previously computed, making this iterator less memory-efficient**. | 2.0 |
	| 8      | make_odd | Speed up the iterations of the Collatz sequences by replacing the successive divisions by 2, by only one step. Be aware that using this "optimization" alone is absolutly not efficient (as you can see, the speedup factor is more or less 1). However, it is a real "booster" when associated with other optimization algorithms. For instance, the *a posteriori* cutoff is boosted with a speedup factor of 3.3 when used together with the "make_odd" one. | 1.0 |
	
	Parameters:
		optimization:
			Type of optimization(s) applied. No optimization by default.
	"""
	
	# Optimizations
	NO_OPT = 0
	EVEN_OPT = 1
	KMOD6_OPT = 2
	APOST_OPT = 4
	MKODD_OPT = 8
	
	def __init__(self, optimization:int = 0):
		self.optimization = optimization
		self.previous_record = -1
		if self.optimization & self.EVEN_OPT:
			self.previous_rank = 0
		if self.optimization & self.APOST_OPT:
			self.records = list()
	
	def __next__(self):
		n = 1
		while True:
			n_discarded = False
			if (self.optimization & self.KMOD6_OPT) and (n%6 == 5):
				# n is not a record in total stopping time
				value = self.previous_record
				n_discarded = True

			if (self.optimization & self.EVEN_OPT) and not n%2:
				if n == self.previous_rank * 2:
					value = self._steps_mkodd(n) if (self.optimization & self.MKODD_OPT) else self._steps_apost(n) if (self.optimization & self.APOST_OPT) else self._steps(n)
					n_discarded = True
				else:
					# n is not a record in total stopping time
					value = self.previous_record
					n_discarded = True
			
			if not n_discarded:
				value = self._steps_mkodd(n) if (self.optimization & self.MKODD_OPT) else self._steps_apost(n) if (self.optimization & self.APOST_OPT) else self._steps(n)
			
			if value is not None and (value > self.previous_record):
				self.previous_record = value
				if self.optimization & self.EVEN_OPT:
					self.previous_rank = n
				if self.optimization & self.APOST_OPT:
					self.records.append(Record(rank=n, value=value))
				return n
			n += 1
	
	def _steps(self, n:int) -> int:
		"""
		The total stopping time of the Collatz sequence beginning by `n`.
		
		Since the values of the Collatz sequence are not stored, the usage of a syracuse.Syracuse() instance is not necessary.
		
		Parameters:
			n:
				Initial value of the Collatz sequence for which the total stopping time is calculated.
		
		Returns:
			The total stopping time.
		
		Raises:
			ValueError:
				Raises if `n` is not a strictly positive integer.
		"""
		
		if n<=0 or not isinstance(n, int):
			raise ValueError(f"{n} is not a strictly positive integer")

		steps = 0
		
		while n>1:
			n = n*3+1 if n%2 else n//2
			steps += 1
		
		return steps
	
	def _steps_apost(self, n:int) -> int|None:
		"""
		The total stopping time of the Collatz sequence beginning by `n`, using the *a posteriori* cutoff optimization.
		
		If the *a posteriori* cutoff algorithm concludes that the current Collatz sequence is not a record, then it is immediatly dropped of, and the function returns `None`.
		
		Parameters:
			n:
				Initial value of the Collatz sequence for which the total stopping time is calculated.
		
		Returns:
			The total stopping time, or `None` if the iteration process has been stopped before its end.
		
		Raises:
			ValueError:
				Raises if `n` is not a strictly positive integer.
		"""
		
		if n<=0 or not isinstance(n, int):
			raise ValueError(f"{n} is not a strictly positive integer")

		steps = 0
		
		while n>1:
			if n%2:
				n = n*3+1
				steps += 1
			else:
				n = n//2
				steps += 1
				if len(self.records) > 0:
					upper_records = [record for record in self.records if n < record.rank]
					for record in upper_records:
						if steps + record.value <= self.previous_record:
							return
					
		return steps
	
	def _steps_mkodd(self, n:int) -> int|None:
		"""
		The total stopping time of the Collatz sequence beginning by `n`, using the "make_odd" optimization.
		
		This method implements also the optional, *a posteriori* cutoff optimization.
		
		Parameters:
			n:
				Initial value of the Collatz sequence for which the total stopping time is calculated.
		
		Returns:
			The total stopping time, or `None` if the iteration process has been stopped before its end (if the *a posteriori* cutoff optimization is activated).
		
		Raises:
			ValueError:
				Raises if `n` is not a strictly positive integer.
		"""
		
		if n<=0 or not isinstance(n, int):
			raise ValueError(f"{n} is not a strictly positive integer")

		steps = 0
		
		while n>1:
			if n%2:
				n = n*3+1
				steps += 1
			
			# At this step, n is necessarily even
			n>>=(p := bit_scan1(n)) # successive divisions by 2
			steps += p
			
			# Optional, *a posteriori* cutoff optimization
			if (self.optimization & self.APOST_OPT):
				if len(self.records) > 0:
					upper_records = [record for record in self.records if n < record.rank]
					for record in upper_records:
						if steps + record.value <= self.previous_record:
							return

		return steps

class max_value_records(Iterator):
	"""
	Sequence of starting values of Collatz sequences with maximum values higher than of any smaller starting value. OEIS reference: [A006884](https://oeis.org/A006884).
	
	!!! example
	
		7 is included in this sequence because the maximum value of the Collatz sequence beginning by 7 (that is, 52) is greater than maximum values of all Collatz sequences beginning by 1, 2, 3, 4, 5 and 6.
	
	In order to speedup the computation, it is possible to apply optional optimizations. Those optimizations are combinable (by addition of their numbers) for a greater efficiency. Deeper details (including mathematical demontrations) are available in [this article from T. Leavens and M. Vermeulen](https://oeis.org/A006877/a006877_1.pdf).
	
	The available sorts of optimizations are the following (the speedup factor is calculated with the first 40 records. It is only indicative, since it may differ on your own configuration):
	
	| Number | Name | Description | Speedup factor |
	| ------ | ---- | ----------- | -------------- |
	| 0      | None | No optimization | 1.0 |
	| 1      | Odd numbers only | Except 2, there is no even record for max value. So it is not necessary to compute Collatz sequences starting by even values. | 2.0 |
	| 2      | k mod 6 = 5 | If the remainder of the division of the initial value by 6 is 5, then this cannot be a record for the max value. | 1.2 |
	| 4      | *a posteriori* cutoff | A record, if found, is a max value appearing before the iteration process has fallen under the initial value. Hence, once the initial value is reached, it is possible to stop the iteration process. | 8.0 |
	| 8      | make_odd | Speed up the iterations of the Collatz sequences by replacing the successive divisions by 2, by only one step. | 1.9 |
	
	Parameters:
		optimization:
			Type of optimization(s) applied. No optimization by default.
	"""
	
	# Optimizations
	NO_OPT = 0
	ODD_OPT = 1
	KMOD6_OPT = 2
	APOST_OPT = 4
	MKODD_OPT = 8
	
	def __init__(self, optimization:int = 0):
		self.optimization = optimization
		self.previous_record = -1
	
	def __next__(self):
		n = 1
		while True:
			if n%2 == 0:
				if (self.optimization & self.ODD_OPT) and (n!=2):
					# n is not a record in max value
					value = self.previous_record
				else:
					value = self._max_mkodd(n) if (self.optimization & self.MKODD_OPT) else self._max(n)
			elif (self.optimization & self.KMOD6_OPT) and (n%6 == 5):
				# n is not a record in max value
				value = self.previous_record
			else:
				value = self._max_mkodd(n) if (self.optimization & self.MKODD_OPT) else self._max(n)
			
			if value > self.previous_record:
				self.previous_record = value
				return n
			
			n += 1
	
	def _max(self, n:int) -> int:
		"""
		The maximum value of the Collatz sequence beginning by `n`.
		
		Since the values of the Collatz sequence are not stored, the usage of a syracuse.Syracuse() instance is not necessary.
		If the *a posteriori* cutoff optimization is enabled, the search for the max value is stopped when the iteration falls below the initial value.
		
		Parameters:
			n:
				Initial value of the Collatz sequence for which the maximum value is calculated.
		
		Returns:
			The absolute maximum value or the the maximum value reached before fallen below the initial value (if the *a posteriori* cutoff optimization is enabled).
		
		Raises:
			ValueError:
				Raises if `n` is not a strictly positive integer.
		"""
		
		if n<=0 or not isinstance(n, int):
			raise ValueError(f"{n} is not a strictly positive integer")
		
		initial_value = n
		max_value = n
		
		while n>1:
			if n%2:
				n = n*3+1
				max_value = max(max_value, n)
				if (self.optimization & self.APOST_OPT) and (n < initial_value):
					break
			else:
				n = n//2
		
		return max_value
	
	def _max_mkodd(self, n:int) -> int:
		"""
		The maximum value of the Collatz sequence beginning by `n`, using the "make_odd" optimization.
		
		This method implements also the optional, *a posteriori* cutoff optimization.
		
		Parameters:
			n:
				Initial value of the Collatz sequence for which the maximum value is calculated.
		
		Returns:
			The absolute maximum value or the the maximum value reached before fallen below the initial value (if the *a posteriori* cutoff optimization is enabled).
		
		Raises:
			ValueError:
				Raises if `n` is not a strictly positive integer.
		"""
		if n<=0 or not isinstance(n, int):
			raise ValueError(f"{n} is not a strictly positive integer")
		
		initial_value = n
		max_value = n
		
		while n>1:
			if n%2:
				n = n*3+1
			# At this step, n is necessarily even
			max_value = max(max_value, n)
			n>>=bit_scan1(n) # successive divisions by 2
			if (self.optimization & self.APOST_OPT) and (n < initial_value):
				break
		
		return max_value