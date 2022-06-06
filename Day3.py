{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vector x [1, 5, 5, 2, 9]\n",
      "Vector y [-1, 3, 15, 27, 29]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x =[1,5,5,2,9]\n",
    "y = [-1,3,15,27,29]\n",
    "\n",
    "print(\"Vector x\",x)\n",
    "print(\"Vector y\",y)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12 14 16 18 20]\n"
     ]
    }
   ],
   "source": [
    "#Ex2:\n",
    "n = int(input(\"The number of elements: \"))\n",
    "# a)\n",
    "x = np.arange(12,12+n*2,2)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vector  [1, 2, 3, 98, 12, 33]\n"
     ]
    }
   ],
   "source": [
    "#Ex4:\n",
    "x = [1,2,3]\n",
    "y = [98,12,33]\n",
    "x.extend(y)\n",
    "z = x\n",
    "print(\"Vector z:\",z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vector z: [[1, 2, 3], [4, 5, 6]]\n"
     ]
    }
   ],
   "source": [
    "#Ex5\n",
    "x = [1,2,3]\n",
    "y = [4,5,6]\n",
    "z = [x,y]\n",
    "print(\"Vector z:\",z)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Ex6\n",
    "x = np.arange(0,22,2)\n",
    "print(x)\n",
    "##a)\n",
    "print(\"The first sixth elements in the vector x:\",x[0:5:1])\n",
    "##b)\n",
    "print(\"The last fifth elements in the vector x:\",x[-5::1])\n",
    "##c)\n",
    "print(\"1st Element : \",x[0])\n",
    "print(\"4th Element : \",x[4])\n",
    "print(\"Last Element : \",x[len(x)-1])\n",
    "##d)\n",
    "print(\"The last fifth elements in the vector x:\",x[0:7:2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximize:  407\n",
      "Minimize:  -131\n",
      "Elements greater than 10 (array([ 1,  7,  9, 12, 13, 14], dtype=int64),)\n"
     ]
    }
   ],
   "source": [
    "#Ex7\n",
    "x = [3 ,11 ,-9 ,-131, -1 ,1 ,-11, 91 ,-6, 407 ,-12 ,-11, 12, 153 ,371]\n",
    "\n",
    "##a)\n",
    "print(\"Maximize: \",max(x))\n",
    "##b)\n",
    "print(\"Minimize: \",min(x))\n",
    "##c)\n",
    "ax = np.array(x)\n",
    "print(\"Elements greater than 10\",np.where(ax>10))\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "cf6663ca35ebd57d6121109460e534e72c1e1f8ff142ad985cdcb4b7e585eb79"
  },
  "kernelspec": {
   "display_name": "Python 3.9.9 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.9"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
