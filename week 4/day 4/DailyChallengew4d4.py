 matrix = [
     ["7"," ","3"],
     ["T","s","i"],
     ["h","%","x"],
     ["i","#"," "],
     ["s"," ","M"],
     ["$","a"," "],
     ["#","t","%"],
     ["i","r","!"]

     ]

 char_count = 0

   for col in range(3):
       for row in range(8):
           current_char = matrix[row][col]
           if isinstance(current_char, int):
               continue

           if current_char.isalnum():
               if char_count >= 2:
                   result += " "
                    count = 0
               result += current_char
           else:
              char_count += 1
                  
   print(result)
    
   
    
    
    
   