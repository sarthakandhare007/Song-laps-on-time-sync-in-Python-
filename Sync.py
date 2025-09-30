 import time
import sys
def type_lyric(line, char_delay=0.065):
 for char in line:
 print(char, end='', flush=True)
 time.sleep(char_delay)
 print()
def print_lyrics():
 lyrics = [
 "Dil jo tumhara hai,",
 "Kaisa bechara hai,",
 "Maane na besharam, bilkul khatara hai,",
 "Tu kare dil beqaraar,",
 "Kyun karoon main tujhse pyar"
 ]
 delays = [1.5, 1.5, 2.0, 1.8, 2.3]
 time.sleep(1.5)
 for i, line in enumerate(lyrics):
 type_lyric(line)
 time.sleep(delays[i])
print_lyrics()
