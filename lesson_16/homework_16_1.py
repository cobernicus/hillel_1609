import pytest

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

team_lead_attributes = TeamLead("Alice", 10000, "Engineering", "Python", 10)
print(team_lead_attributes)
@pytest.mark.parametrize("actual, expected", [
    (team_lead_attributes.name, "Alice"),
    (team_lead_attributes.salary, 10000),
    (team_lead_attributes.department, "Engineering"),
    (team_lead_attributes.programming_language, "Python"),
    (team_lead_attributes.team_size, 10)
])
def test_team_lead_attributes(actual, expected):
    assert expected == actual
