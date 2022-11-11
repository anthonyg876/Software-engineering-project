import db
import pytest



def test_addUser1():

    db.addUser("user981@gmail.com", "User981First", "User981Last", 0, "user981pass")

    last_record = db.return_all_participants()[-1]

    assert last_record[0] == "user981@gmail.com"


def test_addUser2():

    db.addUser("user981@gmail.com", "User981First", "User981Last", 0, "user981pass")

    last_record = db.return_all_participants()[-1]

    assert last_record[1] == "User981First"  


def test_addUser3():

    db.addUser("user981@gmail.com", "User981First", "User981Last", 0, "user981pass")

    last_record = db.return_all_participants()[-1]

    assert last_record[4] == "user981pass"  


def test_addBusiness1():

    db.addBusiness("seller40004@gmail.com", 40004, "Business40004", "pass40004", "address40004", "c40004", 123456789)

    last_record = db.return_all_businesses()[-1]

    assert last_record[0] == 40004


def test_addBusiness2():

    db.addBusiness("seller40005@gmail.com", 40005, "Business40005", "pass40005", "address40005", "c40005", 123456789)

    last_record = db.return_all_businesses()[-1]

    assert last_record[2] == "pass40005"

    

def test_updateBusiness1():

    db.updateBusinessName(40005,"UpName")

    last_record = db.return_all_businesses()[-1]

    assert last_record[1] == "UpName"


def test_updateBusiness2():

    db.updateBusinessPhoneNumber(40005, 9991234511)

    last_record = db.return_all_businesses()[-1]

    assert last_record[5] == 9991234511

def test_updateIncome():

    db.updateParticipantsIncome("user981@gmail.com", 50)

    last_record = db.return_all_participants()[-1]

    assert last_record[3] == 50

def test_updateLast():

    db.updateParticipantsLastName("user981@gmail.com", "Jenkins")

    last_record = db.return_all_participants()[-1]

    assert last_record[2] == "Jenkins"

def test_deleteuser():

    db.deleteParticipant("user981@gmail.com")

    last_record = db.return_all_participants()[-1]

    assert last_record[2] != "Jenkins"
