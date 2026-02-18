# How to Run

## Setup
- Create a MongoDB account and cluster.

- Clone the GitHub repository.  
- Locate where the folder is created.  
- Open the folder.

## Activity 1
- On terminal, run:  
```bash
cd Activity1
cd Backend
```

Modify dataBase.py with your MongoDB connection string.

On terminal, run:
```bash
uvicorn main:app --reload
```
Go to the link provided by Uvicorn and add /docs at the end.

Click on /dummy-users/.
<img width="1918" height="115" alt="image" src="https://github.com/user-attachments/assets/8c452960-5488-40ba-8116-3e3d99111739" />

Click Try it out and then Execute.
<img width="1801" height="305" alt="image" src="https://github.com/user-attachments/assets/cbac9661-8f2b-49a6-b272-a8acd03e4008" />

Check your MongoDB cluster to see if the dummy users were generated.
<img width="1452" height="682" alt="image" src="https://github.com/user-attachments/assets/b4782b84-1676-4cb0-b566-d98719b278ad" />
