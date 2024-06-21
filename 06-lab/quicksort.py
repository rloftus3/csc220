# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

listVisits = 0

def inplace_quick_sort(S, a, b):
  """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
  global listVisits
  if a >= b: return                                      # range is trivially sorted

  listVisits += 1
  pivot = S[b]                                           # last element of range is pivot
  left = a                                               # will scan rightward
  right = b-1                                            # will scan leftward
  while left <= right:
    # scan until reaching value equal or larger than pivot (or right marker)
    while left <= right:
      listVisits += 1
      if S[left] < pivot:
        left += 1
      else: 
        break
    # scan until reaching value equal or smaller than pivot (or left marker)
    while left <= right:
      listVisits += 1
      if pivot < S[right]:
        right -= 1
      else:
        break
    if left <= right:                                    # scans did not strictly cross
      listVisits += 4
      S[left], S[right] = S[right], S[left]              # swap values
      left, right = left + 1, right - 1                  # shrink range

  # put pivot into its final place (currently marked by left index)
  listVisits += 4
  S[left], S[b] = S[b], S[left]
  # make recursive calls
  inplace_quick_sort(S, a, left - 1)
  inplace_quick_sort(S, left + 1, b)

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Rachel Loftus
# there is nothing below here!