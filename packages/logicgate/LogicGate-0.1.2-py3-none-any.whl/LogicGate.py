from os.path import exists
from sys import argv
import sys
from random import randint


def run(
  filename: str,
  gate: bool = False,  #show gate in result
  ascii: bool = True,  #show ascii in result
  debug: bool = False,  #log during process
  check: str = ''  #check for error in code, mostly for debug
) -> int:  #returns exit code for some reason lol
  """To run this filename is the only thing needed, Error code will be returned. if everything works fine, output will be printed. and 0 will be returned.
  
  Arguments, type of input, usecases:
      filename: string, specify which file needed to run
      gate: boolean(True or False), if the result shows gate result or not
      ascii: boolean, if the result converts to ascii and show or not
      debug: boolean, show the unhuman log during the interpute
      check: string, if it is specified then the result will be colored. It compares the difference between the gate result and the binary of check input, only works if both gate and ascii is True 
             (color: green=correct bit
                     red=incorrect bit
                     blue box=missing bit 1
                     purple box=missing bit 0)
                     """

  def process(
    obj,  #first command
    line: tuple = (
      0, 0
    ),  #for error reporting, first is line and second is index, sometimes third for the latest gate called
    aft=None,  #command afterward
    an=None,  #None/True/False -> (1/0/Not)/And/Or
  ) -> tuple:  #(0 or 1, unprocessed commands that may be used by and/or gates in previous commands in list)
    'One line code processor, return one output from a line of input, internal use only'
    if debug: print('called, args:', obj, line, aft, an)
    if len(str(obj)) == 1:  #if the first process string is a single command
      obj = str(obj)
      AnList = None
      if an != None:
        #if AnList exists, it is an and/or gate, depends on the first index is True(and) or False(or)
        AnList = [an]
        if debug: print('AnList init:', AnList)
      if obj == '1':
        if debug: print('1:', aft)
        if AnList:
          AnList.append((1, aft))
        else:
          return (1, aft)
      elif obj == '0':
        if debug: print('0:', aft)
        if AnList:
          AnList.append((0, aft))
        else:
          return (0, aft)
      if aft != None and aft != []:
        if debug: print('gate sector for', obj)
        if obj == 'N':
          proc = process(aft[0], line=(line[0], line[1] + 1, 'N'), aft=aft[1:])
          if debug: print('not:', proc)
          if AnList:
            AnList.append((0 if proc[0] else 1, proc[1]))
          else:
            return (0 if proc[0] else 1, proc[1])
        elif obj == 'A':
          proc = process(aft[0],
                         line=(line[0], line[1] + 1, 'A'),
                         aft=aft[1:],
                         an=True)
          if debug: print('and:', proc)
          if AnList:
            AnList.append(proc)
          else:
            return tuple(proc)
        elif obj == 'O':
          proc = process(aft[0],
                         line=(line[0], line[1] + 1, 'O'),
                         aft=aft[1:],
                         an=False)
          if debug: print('or:', proc)
          if AnList:
            AnList.append(proc)
          else:
            return tuple(proc)
      if AnList != None:
        if debug: print('And/Or gate:', AnList)
        try:
          if AnList[1][1] == None:
            raise IndexError()
          AnList.append(
            process(
              AnList[1][1][0],
              line=(line[0], line[1] + 1, 'A' if AnList[0] else 'O'),
              aft=None if len(str(AnList[1][1])) == 1 else AnList[1][1][1:]))
        except IndexError:
          sys.tracebacklimit = 0
          raise SyntaxError(
            f'gate {line[2] if obj=="0" or obj=="1" else obj} in line {line[0]} index {line[1]-1} requires {"1" if (line[2] if obj=="0" or obj=="1" else obj)=="N" else "2"} inputs, 1 received'
          )
        if len(AnList) == 3:
          if AnList[0]:
            return (AnList[1][0] and AnList[2][0], AnList[2][1])
          else:
            return (AnList[1][0] or AnList[2][0], AnList[2][1])
      else:
        #and/or gate syntax error
        sys.tracebacklimit = 0
        raise SyntaxError(
          f'gate {line[2] if obj=="0" or obj=="1" else obj} in line {line[0]} index {line[1]} requires {"1" if (line[2] if obj=="0" or obj=="1" else obj).upper()=="N" else "2"} inputs, 0 received'
        )
    else:
      #if the first command given is not one command
      raise SystemError(
        'Internal error, unexpected arguments received in internal helper function, please do not change the code'
      )

  if exists(filename):
    with open(filename, 'r') as f:
      Out = [[]]
      dt = f.readlines()
      if filename[-6:] != '.lgeso':
        print(
          f'{filename} is not an lgeso file, maybe renaming the file extension to lgeso and try again'
        )
        return 1
      for dtidx, line in enumerate(dt):
        line = line.replace('\n', '')
        if '---' in line:
          Out.append([])
        elif '###' in line:
          continue
        else:
          Out[-1].append(
            str(
              process(line[0],
                      line=(dtidx + 1, 1),
                      aft=(None if len(line) == 1 else line[1:]))[0]))
      hold = ""
      checkhold = []
      if check:
        for char in check:
          checkhold.append(str(bin(ord(char))[2:]))
      if gate:
        print('gates result:')
      for nidx, n in enumerate(Out):
        Nhold = n.copy()
        if n == []:
          continue
        if gate:
          for chekidx, chek in enumerate(n):
            if '\033[0;37;41m' in chek and '\033[0;37;40m' in chek:
              continue
            if chek != '1' and chek != '0' and chek != ' ':
              print(
                f'error char {repr(chek)} found in index {chekidx}, line {nidx+1}, please report that line of code shown in lgeso file to the dev. '
              )
            if ascii and check:
              if nidx >= len(checkhold):
                n[chekidx] = f'\033[0;37;41m{chek}\033[0;37;40m'
              else:
                if len(n) > len(checkhold[nidx]):
                  for _ in range(len(n)-len(checkhold[nidx])):
                    checkhold[nidx] = '0' + checkhold[nidx]
                if chek != checkhold[nidx][chekidx]:
                  n[chekidx] = f'\033[0;37;41m{chek}\033[0;37;40m'
                else:
                  n[chekidx] = f'\033[0;37;42m{chek}\033[0;37;40m'
          if nidx < len(checkhold):
            if len(n) < len(checkhold[nidx]):
              for x in checkhold[nidx][len(n):]:
                n.append(f'\033[0;37;{"46" if int(x) else "45"}m▯\033[0;37;40m')
          n.append(' ')
          print(''.join(n))
        if ascii:
          try:
            hold += chr(int(''.join(Nhold), 2))
          except ValueError:
            print(
              f'unacceptable ascii result received, ascii code: {"".join(Nhold), 2}'
            )
      if ascii:
        print("\nAscii converted result:\n" + hold)
        if gate and check:
          print('\nExpected result:\n' + check)
      return 0
  else:
    print(
      f'{filename} is not an existing file from given path, prehaps try moving the file to the same directory as this program?'
    )
    return 1


def compile(
  filename: str = 'main.lgeso',
  output: str = 'Hello World!',
  randomize: bool = True,
  random_range: list = [1, 5],
  pure_random: list = []
) -> None:  #I swear if this thing returns anything somehow somewhere and somewhat, python is dying or my brain is dying
  """compile string to lgeso file, random_range is needed only when randomize is true.
  filename: string, specify which file to write the data into, new file named as filename will be created if it doesn't exist
  output: string, specify what result will be produced
  randomize: boolean, if the data written is pure binary or further encrypted with gates
  random_range: list, the maximum set of gates in the written data will be the square of the second item while the minimum will be the square of the first item.
  pure_random: boolean, if the """

  if not output:
    output = 'Hello World!'
  if filename:
    if len(filename) > 6:
      if filename[-6:] != '.lgeso':
        print(f'filename is not an lgeso file, filename changed to {filename}')
        filename += '.lgeso'
    elif '.' in filename:
      print(f'filename is not an lgeso file, filename changed to {filename}')
      filename += '.lgeso'
    else:
      print(f'filename is not an lgeso file, filename changed to {filename}')
      filename = 'main.lgeso'
  else:
    print(f'filename is not an lgeso file, filename changed to {filename}')
    filename = 'main.lgeso'
  with open(filename, 'w') as f:
    if len(random_range) != 2 or random_range[0] > random_range[1]:
      print('invalid random range received, changed to 1-5')
      random_range = [1, 5]  #when the random_range is not correctly formatted
    for checkidx, check in enumerate(random_range):
      try:
        random_range[checkidx] == int(check)  #if the input is a number or not
      except ValueError:
        print('invalid random range received, changed to 1-5')
        random_range = [1, 5]
        break
      else:
        if check < 1 or check > 1000:  #avoid too many looping
          print(
            'an item in random range is too large or too small, changed to 1-5'
          )
          random_range = [1, 5]
          break
    for char in output:
      line = str(bin(ord(char))[2:])
      for char in line:
        if randomize:
          charGoal = int(char)  #the ideal final output after the randomizing
          for _ in range(
              randint(random_range[0], random_range[1]) *
              randint(random_range[0], random_range[1])):
            gates = randint(0, 3)
            if gates == 1:
              char = ('N0' if char == '1' else 'N1' if char == '0' else
                      ('NN' + char))
            elif gates == 2:
              buff = ('1' if randint(0, 1) else '0') if charGoal else '0'
              char = 'O' + (char + buff if randint(0, 1) else buff + char)
            elif gates == 3:
              buff = '1' if charGoal else ('1' if randint(0, 1) else '0')
              char = 'A' + (char + buff if randint(0, 1) else buff + char)
        f.write(char + '\n')
      f.write('---\n')
    print(
      f'compilation completed and result written in {filename} with output as {output}.\nrandomizaion is {"on" if randomize else "off"}\n\n\n'
    )


if __name__ == '__main__':
  exit(run((str(argv[1]) if len(argv) != 1 else 'main.lgeso')))
