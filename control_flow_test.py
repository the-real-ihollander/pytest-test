from control_flow import admin_login, hows_the_weather, fizzbuzz


def test_admin_login():
    # returns "Access granted" if the username is "admin" and the password is "12345"
    assert admin_login("admin", "12345") == "Access granted"

    # returns "Access granted" if the username is "ADMIN" and the password is "12345"
    assert admin_login("ADMIN", "12345") == "Access granted"

    # returns "Access denied" for all other username/password combinations
    assert admin_login("sudo", "12345") == "Access denied"
    assert admin_login("admin", "sudo") == "Access denied"
    assert admin_login("sudo", "pls") == "Access denied"


def test_hows_the_weather():
    # returns "It\'s brisk out there!" if the temperature is below 40
    assert hows_the_weather(33) == "It's brisk out there!"

    # returns "It\'s a little chilly out there!" if the temperature is between 40 and 65
    assert hows_the_weather(55) == "It's a little chilly out there!"

    # returns "It\'s too dang hot out there!" if the temperature is above 85
    assert hows_the_weather(99) == "It's too dang hot out there!"

    # returns "It\'s perfect out there!" for all other temperatures
    assert hows_the_weather(77) == "It's perfect out there!"


def test_fizzbuzz():

    # returns "FizzBuzz" when the input is a multiple of 3 and 5
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"

    # returns "Fizz" when the input is a multiple of 3
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

    # returns "Buzz" when the input is a multiple of 5
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

    # returns the number when the input not is a multiple of 3 or 5
    assert fizzbuzz(4) == 4
    assert fizzbuzz(7) == 7
