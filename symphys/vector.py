import numpy as np

def dot(v1, v2):
	""" Evaluate the dot product of the given vectors

	Parameters
	----------
	v1 : Vector
		A Vector object
	v2 : Vector
		A Vector object

	Returns
	-------
	dot : float
		The dot product of the given vectors
	"""
	return np.sum(v1.vector*v2.vector)

def cross(v1, v2):
	""" Evaluate the cross product of the given vectors

	Parameters
	----------
	v1 : Vector
		A Vector object
	v2 : Vector
		A Vector object

	Returns
	-------
	v3 : Vector
		The resulting Vector from crossing the given ones
	"""
	return Vector(np.cross(v1.asRow().vector, v2.asRow().vector))

def tripProd(v1, v2, v3):
	""" Evaluates the triple product of the given three vectors, in order

	Parameters
	----------
	v1 : Vector
		A Vector object
	v2 : Vector
		A Vector object
	v3 : Vector
		A Vector object

	Returns
	-------
	trip : float
		The resulting number from taking the triple product of the given vectors
	"""
	return dot(v1, cross(v2, v3))

def tripVecProd(v1, v2, v3):
	""" Evaluates the triple vector product of the given three vectors, in order

	Parameters
	----------
	v1 : Vector
		A Vector object
	v2 : Vector
		A Vector object
	v3 : Vector
		A Vector object

	Returns
	-------
	trip : float
		The resulting number from taking the triple vector product of the given vectors
	"""
	return cross(v1, cross(v2, v3))


class Vector(object):
	""" A vector, with magnitude and direction

	Attributes
	----------
	vector : numpy.array
		A numpy array representing the vector under the hood
	"""

	def __init__(self, li, row=False):
		""" Constructor. Takes in a list, converts to proper numpy array

		Parameters
		----------
		li : list
			A 
		"""
		if row:
			self.vector = np.asarray(li)
		else:
			self.vector = np.asarray([li]).reshape(len(li), 1)

	def __str__(self):
		return str(self.vector.reshape(len(self.vector), ))

	def __setitem__(self, ind, value):
		""" Set values with square brackets
		"""
		if type(ind) is int:
			self.vector[ind][0] = value
		else:
			raise KeyError

	def __getitem__(self, ind):
		""" Get values with square brackets
		"""
		if type(ind) is int:
			return self.vector[ind][0]
		else:
			raise KeyError

	def dim(self):
		""" The dimensionality of the vector
		"""
		return len(self.vector)

	def asRow(self):
		""" Returns the vector as a row vector
		"""
		return Vector(self.vector.reshape(len(self.vector), ), row=True)

class Point(Vector):
	""" A point. Subclass of Vector with magnitude 0
	"""


