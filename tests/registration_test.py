import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['LOGIN_DISABLED'] = True
        lm.init_app(app)
        self.app = app.test_client()
        db.create_all()

    # I have tried setting priority as int and string.
    def ticket(self, title, content, priority=1, category=1):
        return self.app.post('flicket/ticket_create/', data=dict(
            title=title,
            content=content,
            priority=priority,
            category=category
        ), follow_redirects=True)

    def test_ticket_creation(self):
        self.login('john_123', '12345')

        title = 'some random title'
        content = 'some random ceontent'
        rv = self.ticket(title, content)
        dump_to_tmp(rv.data.decode(), 'dump.html')




















