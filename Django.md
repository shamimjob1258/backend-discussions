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
2. Use model viewset to create apis
3. Write api to add data to student model
4. Add filter functionality using DjangoFilterBackend
5. Use serilizer for the apis.
6. on the details api of the student get all mark details


# Task 1 instructions:
    1. Install django
    2. Create app called Student.
    3. Install rest-framework
    4. Install DjangoFilterBackend


# Task 2:
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


  1. Create apis for CreditFeedback and Transaction.
  2. When transaction is created only get invoice_date and due_date from frontend.
  3. api to change the status of the transaction
  3. When Transaction details is api is called.
      case1:
            1. Id transaction is SUBMITTED status get the latest intersest_rate and processing_fee 
               from CreditFeedback in transaction details api
            2. If Transaction is ACCEPTED status, Transaction details
                api should return the rates in which the Transaction got approved.
