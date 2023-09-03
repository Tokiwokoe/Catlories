# Catlories - Food diary
Personal food diary to track your diet. It can help to know calorie and macronutrients count in certain meal and adjust nutrition if needed.
Body data analysis automatically calculates the required amount of calories, proteins, fats and carbs depending on the selected goal: to lose, maintain or gain weight.

Python, Django, PostgreSQL, Django REST Framework, HTML, CSS

# Quickstart
### Installing git and cloning repository
    git clone https://github.com/Tokiwokoe/Catlories.git
    cd Catlories
### Setting virtual environment
    python -m venv venv
    \venv\Scripts\activate
    pip install -r requirements.txt
### Copy environment variables to .env and fill it with your values
    cp .env.template .env
### Run the app localy
    python manage.py runserver

# Usage
### Sign up or sign in
You must create an account to use the diary. On the main page in header there is a button "Зарегистрироваться" that you can click to sign up. Or you can click on "Войти в аккаунт" to sign in if you already have an account.

In sign up page you should fill the form with the parameters of your body. It is necessary to build your diet plan.

### Statistics page
Here you can see your and daily amount of calories you should consume and your body mass index. All that values are calculated using data from your profile.

### Diary page
Here you can add meals in your diary by clicking on breakfast, lunch, dinner or snack. The next step you need to enter barcode of the food (it is usually located on the back of the package).
Now you have two options: add the food in favorites or in your diary.

### Favorites
There are your favorite meals. You can add more or delete something.

### Your profile
This page contains information about you. Nobody can see it but you. You can also change your profile data if needed.