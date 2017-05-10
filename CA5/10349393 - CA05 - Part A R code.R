# sum function, adds numbers together
sum_func <- function(n1, n2){
  return(n1 + n2)
}

sum_func(1,2) # returns 3

# subtract function, takes one number from another
subtr_func <- function(n1, n2){
  return(n1 - n2)
}

subtr_func(3,2) # returns 1

# multiples two numbers
mult_func <- function(n1, n2){
  return(n1 * n2)
}

mult_func(2,3) # returns 6


# divides one number by another, watches for division by zero error
div_func <- function(n1, n2){
  if(n2 == 0){
    result <- NA
  }
  else {
    result <- (n1 / n2)
  }
  return(result)
}

div_func(3,0) # returns Na
div_func(10,2.5) # returns 4
div_func(4,3) # returns 1.333...

# returns one number to the power of a second
power_func <- function(n1, n2){
  return(n1 ** n2)
}

power_func(4,2) # returns 16

# this returns the square of one number
sq_func <- function(n1){
  return(n1 ** n1)
}

sq_func(4)  # return 256

# this returns the square root of a number, it watches for negative numbers and zero to prevent errors
sqrt_func <- function(n1){
  if(n1 <= 0){
    result <- NA
  }
  else {
    result <- sqrt(n1)
  }
  return(result)
}

sqrt_func(16) #returns 4

# returns the sine of passed degrees.
sindeg_func <- function(n1){
  return(sin(n1*pi/180))
}

sindeg_func(30) # returns 0.5

# returns the cosine of passed degrees. 
cosdeg_func <- function(n1){
  return(cos(n1*pi/180))
}

cosdeg_func(30) # returns 0.8660254

# returns the factorial of a number, watches for negative numbers and zero to prevent errors
factorial_func <- function(n1){
  if(n1 <= 0){
  result <- "I'm afraid this program can't calculate that"
  }
  else{
  result <- factorial(n1)
  }
  return(result)
}

factorial_func(8) # returns 40320
