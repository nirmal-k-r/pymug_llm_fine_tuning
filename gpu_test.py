{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tensor([1.], device='mps:0')\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "if torch.backends.mps.is_available():\n",
    "    mps_device = torch.device(\"mps\")\n",
    "    x = torch.ones(1, device=mps_device)\n",
    "    print (x)\n",
    "elif torch.cuda.is_available():\n",
    "    print (\"MPS device not found. Using CUDA device.\")\n",
    "    x = torch.ones(1, device=\"cuda\")\n",
    "    print (x)\n",
    "else:\n",
    "    print (\"MPS device not found.\")"
   ]
  }
 ],
 "metadata": {
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
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
