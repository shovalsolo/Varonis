The following TC is a Sanity flow to test the basic fuctionalty work

Installation process

1. Pull the repo

2. Check if Homebrew is installed
	Run command → brew –version

3. Install Homebrew
	Run command → /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    or
    Run command → brew install python

4. Install python
	Run command → brew install python

5. Verify installation
	Run command → python3 --version

6. Run automation after pulling the repo
    Run command → python3 test_credit_memo.py

7. Run with report
	pytest --html=reports/full_report.html --self-contained-html -v


*** Before running the automation we need to update the following:
1. Download chromedriver and update path in value executable_path in line 10
2. NetSuite URL:
3. NetSuite User: 
4. NetSuite User Password:
