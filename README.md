# keyAlarm
A program that prevents you from typing too much.

I created this program to help me with health problems. It will only work on linux and not on wayland. It will only disable your keyboard if you change the xinput keyboard name to the name of your keyboard: `xinput list`

The program works as follows:
There is a countdown of, lets say, 100 key presses, and every time you press a key, the countdown goes down by one.
Every, lets say second, it recovers 1 key. 
When it reaches like 20 keys, it spams you with notifications.
When it reached 0, you get a typing timeout (the keyboard will be disabled until the key countdown has fully recovered to 100 again.

This program helped me a lot because it forced me to, type more efficiently, use more efficient shortcuts and to think about code before I wrote it more than I usually do.

So far I have been too lazy to make this program useable for other people, but someone on HN asked me to share it anyways, so it is on github now. Feel free to steal the idea of this program.
