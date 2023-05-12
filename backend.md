# Task 1:
1. Create 

        * Model 1(Student)
            - name
            - age,
            - marks (m2m)
            - standard

        * Model 2(Marks)
            - subject
            - marks
2. Write apis to create Student with marks.
3. api for retriving  student details.

Task2:

       Model: Transaction 
              invoice amount: float 
              due_date: datetime
              intersest_rate: float 
              processsing_fee: float
              status: choise field [SUBMITTED, ACCEPTED]
              accepted_date: datetime


       Model: CreditFeedback:
           intersest_rate: float 
           processsing_fee: float 


 # Task 1 :

  1. Create apis for CreditFeedback and Transaction.
  2. When transaction is created only get invoice_date and due_date from frontend.
  3. api to change the status of the transaction
  3. When Transaction details is api is called.
      case1:
            1. Id transaction is SUBMITTED status get the latest intersest_rate and processing_fee 
               from CreditFeedback in transaction details api
            2. If Transaction is ACCEPTED status, Transaction details
                api should return the rates in which the Transaction got approved.
