print("Enter the which Test type you want to run")
test_type = input("Enter the test type: API,UI,Performance, Security ")

match test_type:
    case "API":
        print("We are running a PostMan API Testcase.")
    case "UI":
        print("We are running a  Selenium Testcase.")
    case "Performance":
        print("We are running a  Performance Testcase.")
    case "Security":
        print("We are running a  Security Testcase.")
    case _:
        print("Invalid Test Type")


# Same case we can do with if else also ,
# if  we have multiple conditions more than 10 for ex : use match otherwise
# if else is fine

