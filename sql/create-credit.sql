create table credits (
  credit_id varchar(50) primary key not null,
  college_enrollment decimal,
  semesters int,
  credit_type varchar(10),
  payment_fee_while_studying decimal,
  payment_fee_after_studying decimal
);