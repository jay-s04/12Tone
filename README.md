# 12Tone
Hello there, this is a small project I created in order to generate 12tone rows.

To start, you have to enter the prime row and reference pitch.
After this, you can enter whatever transformations you would like to do to your row.

- P:
Entering a P will return the prime row

- 7[or any number from 0-11]:
Entering any integer value between 0 and 11 will transpose your row up by that many semitones. For example, if a row that uses G as its first pitch is transposed up 2, it will use A as its first pitch, move all the other pitches up by 2.

- I:
Our next way to transform a 12 tone row is an inversion. Inverting the row changes each pitch to go down from the reference pitch instead of going up. Essentially, it takes each pitch and subtracts it from 12.

- R:
A retrograde is a type of transformation where you reverse the entire row. If a row started with 0, 1, 3,.. and we applied a retrograde transformation, the last few notes of the row would become ...,3, 1, 0

- Combination:
We can combine any of these methods because the program loops over each individual character of the user input and applies that transformation to it. If you were to enter RI9, It would return the retrograde inversion of the prime row transposed up by 9 semitones. Inputting anything other than R, I, P, or an integer between 0 and 11 will throw an error and ask you to enter it again.

- Enharmonics:
I have yet to properly implement enharmonics into the program. Currently it will only return the notes C, C#, D, Eb, E, F, F#, G, Ab, A, Bb, B, C


