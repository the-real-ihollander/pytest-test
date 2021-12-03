/*
  Write a method `admin_login` that takes two arguments, a username and a
  password. If the username is "admin" or "ADMIN" and the password is "12345",
  return "Access granted". Otherwise, return "Access denied".
*/
function adminLogin(username, password) {
  if ((username === "admin" || username === "ADMIN") && password === "12345") {
    return "Access granted";
  } else {
    return "Access denied";
  }
}

/*
  Write a method `hows_the_weather` that takes in one argument, a temperature.
  If the temperature is below 40, return "It's brisk out there!". If the temperature is
  between 40 and 65, return "It's a little chilly out there!". If the temperature is above 85,
  return "It's too dang hot out there!". Otherwise, return "It's perfect out there!"
*/
function howsTheWeather(temperature) {
  let response;
  if (temperature < 40) {
    response = "brisk";
  } else if (temperature >= 40 && temperature <= 65) {
    response = "a little chilly";
  } else if (temperature > 85) {
    response = "too dang hot";
  } else {
    response = "perfect";
  }
  return `It's ${response} out there!`;
}

/* 
  Write a method `fizzbuzz` takes in a number. For multiples of three, return
  "Fizz" instead of the number. For the multiples of five, return "Buzz". For
  numbers which are multiples of both three and five, return "FizzBuzz". For
  all other numbers, just return the number itself.
*/
function fizzbuzz(num) {
  if (num % 3 === 0 && num % 5 === 0) {
    return "FizzBuzz";
  } else if (num % 3 === 0) {
    return "Fizz";
  } else if (num % 5 === 0) {
    return "Buzz";
  } else {
    return num;
  }
}
