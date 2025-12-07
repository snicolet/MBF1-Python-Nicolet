{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "source": [
    "# Programmation orientée objet (POO)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "outputs": [],
   "source": [
    "# definition d'une classe\n",
    "class Humain:\n",
    "    \"\"\"\n",
    "    classe de tous les humains\n",
    "    \"\"\"\n",
    "    # constructeur\n",
    "    def __init__(self):\n",
    "        # paramètre self: la méthode __init__ s'applique à l'objet lui-même (itself)\n",
    "        print(\"création d'un objet humain...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "création d'un objet humain...\n",
      "création d'un objet humain...\n"
     ]
    }
   ],
   "source": [
    "# création de deux objets de la classe Humain\n",
    "h1 = Humain()\n",
    "h2 = Humain()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "celltoolbar": "Format de la Cellule Texte Brut",
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
