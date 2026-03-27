---
layout: activity
permalink: /Activities/GraphicsSound
title: "CS170: Programming for the World Around Us - Graphics and Sound with Python"


info:
  goals: 
    - To use graphics and sound capabilities in Python
  models:
    - title: "Graphics"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        from ezgraphics import GraphicsWindow

        win = GraphicsWindow(640, 480)
        win.setTitle("My First Drawing")

        canvas = win.canvas()

        canvas.setFill(255, 0, 0)
        canvas.drawRectangle(40, 40, 100, 200)

        canvas.setFill(255, 255, 255)
        canvas.setOutline(0, 255, 0)
        canvas.drawRectangle(200, 200, 150, 50)

        win.wait()
        ]]></script>  
      questions: 
        - "Run this code in your terminal: <code>http://www.ezgraphics.org/uploads/Software/Download/ezgraphics-2.2.tar.gz && pip install ezgraphics-2.2.tar.gz</code> to install the ezgraphics library, and run this program.  What does it do?"
        - "Experiment with the functions and generate your own shapes.  Can you draw a house or a stick figure?  Make a function that does this, given the <code>x</code> and <code>y</code> midpoint as parameters."
    - title: "Animation"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        from ezgraphics import GraphicsWindow
        import random

        win = GraphicsWindow(640, 480)
        win.setTitle("My First Drawing")

        i = 0
        j = 0
        lasti = -1
        lastj = -1

        canvas = win.canvas()

        canvas.setFill(0,0,0)
        canvas.drawRectangle(0, 0, 640, 480)

        while True:
          if i > 0 and j > 0:
            canvas.setFill(0,0,0)
            canvas.drawRectangle(i-1, j-1, 10, 20)
            
          canvas.setFill(255, 255, 255)
          canvas.drawRectangle(i, j, 10, 20)

          lasti = i
          lastj = j
          
          i = i + random.randint(-1, 1)
          j = j + random.randint(-1, 1)

          if i > 640:
            i = 639
          if j > 480:
            j = 479

          if i < 0:
            i = 1
          if j < 0:
            j = 1

          win.pause(1)
          
        win.wait()
        ]]></script>  
      questions: 
        - "Comment this program; what does it do?  You will find it helpful to run the program first, and may find it helpful to set a breakpoint and use the debugger!"
    - title: "Sound"
      model: |
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        # https://stackoverflow.com/questions/974071/python-library-for-playing-fixed-frequency-sound

        """Play a fixed frequency sound."""
        from __future__ import division
        import math
        from scipy import signal
        from pyaudio import PyAudio # sudo apt-get install python{,3}-pyaudio

        try:
            from itertools import izip
        except ImportError: # Python 3
            izip = zip
            xrange = range

        def sine_tone(frequency, duration, volume=1, sample_rate=22050):
            n_samples = int(sample_rate * duration)
            restframes = n_samples % sample_rate

            p = PyAudio()
            stream = p.open(format=p.get_format_from_width(1), # 8bit
                            channels=1, # mono
                            rate=sample_rate,
                            output=True)
                            
            s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
            samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))

            if duration >= 1:
                sample_size = sample_rate
            else:
                sample_size = int(sample_rate * duration)

            for buf in izip(*[samples]*sample_size): # write several samples at a time
                stream.write(bytes(bytearray(buf)))

            # fill remainder of frameset with silence
            stream.write(b'\x80' * restframes)

            stream.stop_stream()
            stream.close()
            p.terminate()

        def square_tone(frequency, duration, volume=1, sample_rate=22050):
            n_samples = int(sample_rate * duration)
            restframes = n_samples % sample_rate

            p = PyAudio()
            stream = p.open(format=p.get_format_from_width(1), # 8bit
                            channels=1, # mono
                            rate=sample_rate,
                            output=True)

            s = lambda t: volume * signal.square(2 * math.pi * frequency * t / sample_rate)
            samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))

            if duration >= 1:
                sample_size = sample_rate
            else:
                sample_size = int(sample_rate * duration)

            for buf in izip(*[samples]*sample_size): # write several samples at a time
                stream.write(bytes(bytearray(buf)))

            # fill remainder of frameset with silence
            stream.write(b'\x80' * restframes)

            stream.stop_stream()
            stream.close()
            p.terminate()    

        def dtmf_tone(frequency1, frequency2, duration, volume=1, sample_rate=22050):
            n_samples = int(sample_rate * duration)
            restframes = n_samples % sample_rate 

            p = PyAudio()
            stream = p.open(format=p.get_format_from_width(1), # 8bit
                            channels=1, # mono
                            rate=sample_rate,
                            output=True)
                            
            s1 = lambda t: volume * math.sin(2 * math.pi * frequency1 * t / sample_rate)
            s2 = lambda t: volume * math.sin(2 * math.pi * frequency2 * t / sample_rate)
            samples = (int(s1(t) * 0x3f + 0x40) + int(s2(t) * 0x3f + 0x40) for t in xrange(n_samples)) # scale to 0-255

            if duration >= 1:
                sample_size = sample_rate
            else:
                sample_size = int(sample_rate * duration)

            for buf in izip(*[samples]*sample_size): # write several samples at a time
                stream.write(bytes(bytearray(buf)))

            # fill remainder of frameset with silence
            stream.write(b'\x80' * restframes)

            stream.stop_stream()
            stream.close()
            p.terminate()

        def sine_chord(frequencies, duration, volume=1, sample_rate=22050):
            if len(frequencies) >= 6:
                frequencies = frequencies[:6]

            n_samples = int(sample_rate * duration)
            restframes = n_samples % sample_rate 

            p = PyAudio()
            stream = p.open(format=p.get_format_from_width(1), # 8bit
                            channels=1, # mono
                            rate=sample_rate,
                            output=True)

            s = []
            k = len(frequencies)
            for i in range(k):                
                f = frequencies[i]
                sf = lambda t: volume * math.sin((2 * math.pi * f * t / sample_rate))
                s.append(sf)

            z = lambda t: sum([int(x(t) * (2**(8-k)-1) + 2**(8-k)) for x in s])
            samples = (z(t) for t in xrange(n_samples)) # scale to 0-255

            if duration >= 1:
                sample_size = sample_rate
            else:
                sample_size = int(sample_rate * duration)

            for buf in izip(*[samples]*sample_size): # write several samples at a time
                stream.write(bytes(bytearray(buf)))

            # fill remainder of frameset with silence
            stream.write(b'\x80' * restframes)

            stream.stop_stream()
            stream.close()
            p.terminate()    
        ]]></script>  
        <br>
        <script type="syntaxhighlighter" class="brush: python"><![CDATA[
        import sounds

        # https://github.com/cleversonahum/dtmf-generator/blob/main/dtmf-generator.py
        DTMF_TABLE = {
            "1": [1209, 697],
            "2": [1336, 697],
            "3": [1477, 697],
            "A": [1633, 697],
            "4": [1209, 770],
            "5": [1336, 770],
            "6": [1477, 770],
            "B": [1633, 770],
            "7": [1209, 852],
            "8": [1336, 852],
            "9": [1477, 852],
            "C": [1633, 852],
            "*": [1209, 941],
            "0": [1336, 941],
            "#": [1477, 941],
            "D": [1633, 941],
            "dial_tone": [350, 440]
        }

        #sounds.sine_tone(2000, 0.5, volume=0.25)
        #sounds.square_tone(2000, 0.25, volume=0.25)

        sounds.dtmf_tone(*DTMF_TABLE['dial_tone'], 2, volume=0.25) # dial tone: 350, 400
        sounds.dtmf_tone(*DTMF_TABLE['6'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['1'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['0'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['4'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['0'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['9'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['3'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['2'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['6'], 0.25, volume=0.25)
        sounds.dtmf_tone(*DTMF_TABLE['8'], 0.25, volume=0.25)

        C = 261.63
        E = 329.63
        G = 392
        sounds.sine_chord([C, E, G], 1, volume=0.25)
        ]]></script>         
      questions: 
        - "Save these two files into your program (call the first one <code>sounds.py</code> since we <code>import sounds</code> in the second file!) and run it."
        - "Look up DTMF tones; what is this program doing?"
        - "Make a song with some tones and play the program.  You might try this with the microbit to see what kinds of notes it plays when you play a melody; you can copy the frequencies into this program."
        
tags:
  - python
  - graphics
  - sound
  
---

