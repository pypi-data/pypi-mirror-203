import random
import webbrowser

class Jupiter:

    def __init__(self):
        exit = True
        
    def start():
        exit = True
        while exit == True:
            task = input("Hi! My name is Jupiter. How can I help you today? ")
            print("Your Command: " + task)
            if task == 'get coordinates':
                Jupiter.getcoordinates()
            elif task == 'help':
                print("Here is a list of valid commands:  \n get coordinates = Generate random target coordinates for a remote viewing session \n generate target = Generates a random target for a remote viewing session \n license = View licensing \n copyright = View copyright \n credits = View credits \n exit = Exits program")
            elif task == 'generate target':
                Jupiter.generatetarget()
            elif task == 'license':
                Jupiter.license()
            elif task == 'copyright':
                Jupiter.copyright()
            elif task == 'credits':
                Jupiter.credits()
            elif task == 'exit':
                exit = False
            else:
                print("Invalid Command. Type 'help' to see a list of commands")  

    def getcoordinates():
        coordinates = ''
        i = 0

        while i < 8:
            coord = random.randint(0,9)
            coordinates += str(coord)
            i += 1

        coordinates = coordinates[:4] + '/' + coordinates[4:]
        print('Your Target Coordinates are: {}'.format(str(coordinates)))

    def generatetarget():
        targetnumber = random.randint(1,238)
        url = "https://farsight.org/sponsors/PoolA/t{}.html".format(targetnumber)
        webbrowser.open(url)

    def copyright():
        print("""Copyright (c) 2023 Aziz Brown

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files 'planetAI', to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.""")

    def license():
        print('MIT License')

    def credits():
        print('Author: Aziz Brown \n https://kuwindacorp.com/ \n github: https://github.com/sageofnamek')