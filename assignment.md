# Points Calculator

Most fundraising agencies have some kind of points system which rewards the fundraiser for the donors they write.
In this task you are supposed to create a command line program that automates calculating those points.

## Requirements
- Your program should take one argument which is either `test` or the path to a csv file.
    With `test` it should run some unit tests and reports the results.
    With the file argument it should calculate the points awarded to each fundraiser.
- When a file argument is given it should be possible to provide an optional parameter a fundraiser id. e.g. `--fundraiser 12366`
    When this parameter is present the calculation should only be done for that specific Fundraiser ID.
- This is the points scheme. Anything not specifically defined should award 0 points.
    Annual amount from 120
        Age 30+
            0.5 Points
        Age 50+
            1 Points
    Annual amount from 150
        Age 30+
            1 Points
        Age 50+
            2 Points
    Annual amount from 300
        Age 30+
            1.5 Points
        Age 50+
            3 Points

## Hand In
Please provide us with a link to a public github repository contaning your project.
After cloning the repo and installing the requirements the program should be executable from the top level directory of the project by calling `./main ARGS`
You can use any python packages you want just make sure to note which you are using in a `requirements.txt` file.


You should find an example csv file attached in this email.
Feel free to ask questions.
Happy coding!
