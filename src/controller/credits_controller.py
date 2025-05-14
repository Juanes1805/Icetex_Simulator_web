import psycopg2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import SecretConfig
from model.credit import Credit
    
class CreditsController:
    """Controller for managing credits in the database."""

    def get_cursor(self):
        """Connect to the PostgreSQL database"""
        connection = psycopg2.connect(
            host=SecretConfig.PGHOST,
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD
        )

        cursor = connection.cursor()
        return cursor

    def create_table(self):
        """Create the credits table in the database"""
        with open("sql/create-credit.sql", "r") as file:
            consultation = file.read()

        cursor = self.get_cursor()
        cursor.execute(consultation)
        cursor.connection.commit()

    def delete_table(self):
        """Delete the credits table in the database"""
        with open("sql/delete-credit.sql", "r") as file:
            consultation = file.read()

        cursor = self.get_cursor()
        cursor.execute(consultation)
        cursor.connection.commit()

    def insert_credit(self, credit: Credit):
        """Insert a credit into the database"""
        cursor = self.get_cursor()
        cursor.execute(
            """
            INSERT INTO credits (
                credit_id,
                college_enrollment,
                semesters,
                credit_type,
                payment_fee_while_studying,
                payment_fee_after_studying
            ) VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                credit.credit_id,
                credit.college_enrollment,
                credit.semesters,
                credit.credit_type,
                credit.payment_fee_while_studying,
                credit.payment_fee_after_studying,  # Si es None, se inserta como NULL
            ),
        )

        cursor.connection.commit()

    def search_credit(self, credit_id: str) -> Credit:
        """Search for a credit in the database by its ID"""
        cursor = self.get_cursor()
        cursor.execute(
            f"""
            SELECT credit_id, college_enrollment, semesters, credit_type, payment_fee_while_studying,
            payment_fee_after_studying FROM credits WHERE credit_id = '{credit_id}'
            """
        )

        row = cursor.fetchone()

        if row:
            return Credit(
                credit_id=row[0],
                college_enrollment=row[1],
                semesters=row[2],
                credit_type=row[3],
                payment_fee_while_studying=row[4],
                payment_fee_after_studying=row[5]
            )
        else:
            return None

    def update_credit(self, credit: Credit):
        """Update a credit in the database"""
        cursor = self.get_cursor()
        cursor.execute(
            f"""
            UPDATE credits SET college_enrollment = '{credit.college_enrollment}',
            semesters = '{credit.semesters}', credit_type = '{credit.credit_type}',
            payment_fee_while_studying = '{credit.payment_fee_while_studying}',
            payment_fee_after_studying = '{credit.payment_fee_after_studying}'
            WHERE credit_id = '{credit.credit_id}'
            """
        )

        cursor.connection.commit()
