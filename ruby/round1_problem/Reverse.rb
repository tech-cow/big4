# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
#
# Don't use String's reverse method; that would be too simple.
#
# Difficulty: easy.


# =================My try=================
def my_reverse(string)
  index = string.length
  i = 0
  new_string = ""
    while index > 0
      new_string[i] = string[index-1]
      index -= 1
      i += 1
    end
return new_string
end
# ========================================

# =================Website Solution=================
def reverse(string)
    reversed_string = ""

  i = 0
  while i < string.length
    reversed_string = string[i] + reversed_string

    i += 1
  end

  return reversed_string
end
# =================================================

@test
puts("\nTests for #reverse")
puts("===============================================")
    puts(
      'reverse("abc") == "cba": ' + (reverse("abc") == "cba").to_s
    )
    puts(
      'reverse("a") == "a": ' + (reverse("a") == "a").to_s
    )
    puts(
      'reverse("") == "": ' + (reverse("") == "").to_s
    )
puts("===============================================")
