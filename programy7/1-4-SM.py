class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def timeline(self):
        print(f"User name: {self.username}")
        for x, y in enumerate(self.posts):
            print(f"{x}: {y}")


def main():
    johndoe = SocialMediaProfile(username='johndoe')

    addPosts = ["Hello, world!",
                 "Had a great day at the park!",
                 "What's up, Natalie? How are you?"]
    for post in addPosts:
        johndoe.add_post(post)

    print()
    johndoe.timeline()


if __name__ == '__main__':
    main()
