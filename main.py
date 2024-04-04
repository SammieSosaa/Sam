def main():
  # Create an empty arraylist to hold the user's favorite color
  favorite_color = []

  # Get input from the user for their favorite color
  print("Enter your favorite color (separated by spaces):")
  color_input = input().split()

  #Add the entered color to the array list
  favorite_color.extend(color_input)

  #Check if Green is in the list of favorite turtles
  if 'Green' in favorite_color:
      print("Great choices! Green is my favorite color aswell.")

      #Print the user's favorites with an asterisk next to Green
      print("Your favorites:")
      for color in favorite_color:
         if color == 'Green':
             print(f"*{color}")
         else:
             print(f"*{color}")

  #Additional message
      print("One of my favorite too.")
  else:
    #Print the user's favorites without any modification
    print("Your favorite:")
    for color in favorite_color:
       print(f" {color}")

if __name__=="__main__":
   main()