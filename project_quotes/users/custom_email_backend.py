from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False

        # Establish the connection without ssl_context
        self.connection = self.connection_class(
            host=self.host,
            port=self.port,
            timeout=self.timeout,
        )

        if self.use_tls:
            self.connection.starttls(context=self.ssl_context)

        if self.username and self.password:
            self.connection.login(self.username, self.password)

        return True
