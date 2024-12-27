# Starting project

To create and initialize the db file:

```
python manage.py makemigrations
python manage.py migrate
```

---

To run the server and start listening to a port and serving requests:

```
python manage.py runserver
```

---

To load professors data from excel file:
it will store them inside the db file, do not run this command on further runs.

```
python manage.py import_professors path/to/your/excel/file.xlsx
```

---

# APIS

## Signup
POST
```/api/accounts/signup/```
**body:**
```{
  "fullname": "Hani12",
  "student_number": "S1228921d21d1c",
  "email": "magma@dd1dd.1co2m",
  "national_code": "1d21d8920123c",
  "department": "Computer Science",
  "password1": "securePassword123",
  "password2": "securePassword123"
}
```
---
## Login
POST
```/api/accounts/login/```
**body:**
```
{
  "email": "magma@dd1dd.1co2m",
  "password": "securePassword123"
}
```
---
## Get All Users

GET

```/api/accounts/users/```
**body:**
Empty

---
## Test Token
GET
```/api/accounts/test_token/```
**body:**
Empty
**headers:**
```
authorization: Token df2cdd517e39dec5d6ce32c97bf2efa77f619b7c
```
---
## Add Comments
POST
```/api/professors/add_comment/```
**body:**
```
{
  "professor_id": 555,
  "text": "Hello fellow comment"
}
```
**headers:**
```
authorization: Token df2cdd517e39dec5d6ce32c97bf2efa77f619b7c
```
---
## Get a professor w/ comments

GET
```/api/professors/<int:id>/```

**body:**

Empty

---
