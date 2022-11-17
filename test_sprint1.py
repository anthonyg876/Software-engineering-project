import db
import pytest



def test_addUser1():

    db.addUser("zbuyer1@gmail.com", "zBuyer1First", "zBuyer1Last", 0, "zBuyer1pass")

    last_record = db.return_all_participants()[-1]

    assert last_record[0] == "zbuyer1@gmail.com"


def test_addUser2():

    db.addUser("zbuyer2@gmail.com", "zBuyer2First", "zBuyer2Last", 0, "zBuyer2pass")

    last_record = db.return_all_participants()[-1]

    assert last_record[1] == "zBuyer2First"  


def test_addUser3():

    db.addUser("zbuyer3@gmail.com", "zBuyer3First", "zBuyer3Last", 0, "zBuyer3pass")

    last_record = db.return_all_participants()[-1]

    assert last_record[4] == "zBuyer3pass"  


def test_addBusiness1():

    db.addBusiness("seller4@gmail.com", 4, "Seller4", "password4", "Seller4addr", "county4", 123456789)

    last_record = db.return_all_businesses()[-1]

    assert last_record[0] == 4


def test_addBusiness2():

    db.addBusiness("seller5@gmail.com", 5, "Seller5", "password5", "Seller5addr", "county5", 223456789)

    last_record = db.return_all_businesses()[-1]

    assert last_record[2] == "password5"

    

def test_updateBusiness1():

    db.updateBusinessName(5,"NameUpdate")

    last_record = db.return_all_businesses()[-1]

    assert last_record[1] == "NameUpdate"


def test_updateBusiness2():

    db.updateBusinessPhoneNumber(5, 1000000000)

    last_record = db.return_all_businesses()[-1]

    assert last_record[5] == 1000000000

def test_updateIncome():

    db.updateParticipantsIncome("zbuyer3@gmail.com", 500)

    last_record = db.return_all_participants()[-1]

    assert last_record[3] == 500

def test_updateLast():

    db.updateParticipantsLastName("zbuyer3@gmail.com", "UpdateLast")

    last_record = db.return_all_participants()[-1]

    assert last_record[2] == "UpdateLast"

def test_deleteuser():

    db.deleteParticipant("zbuyer3@gmail.com")

    last_record = db.return_all_participants()[-1]

    assert last_record[2] != "UpdateLast"
