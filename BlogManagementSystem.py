from datetime import datetime

class BlogManagementSystem:
    def __init__(self):
        self.blog_posts_cache = {}  # Stores blog posts
        self.comments_cache = {}  # Stores comments for each blog post
        self.user_sessions_cache = {}  # Stores user session data
        self.tags_cache = {}  # Stores tags and their associated blog posts

    def create_blog_post(self, post_id, title, content, tags, author_id):
        """Create a blog post and store it in the blog_posts_cache."""
        post_data = {"title": title, "content": content, "tags": tags, "author_id": author_id}
        self.blog_posts_cache[post_id] = post_data
        
        # Update tags_cache
        for tag in tags:
            if tag not in self.tags_cache:
                self.tags_cache[tag] = []
            self.tags_cache[tag].append(post_id)
        
        print(f"Blog post '{title}' created and cached.")
    
    def add_comment(self, post_id, comment_id, user_id, content):
        """Add a comment to a specific blog post."""
        comment = {
            "comment_id": comment_id,
            "user_id": user_id,
            "content": content,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        if post_id not in self.comments_cache:
            self.comments_cache[post_id] = []
        
        self.comments_cache[post_id].append(comment)
        print(f"Comment added to post '{post_id}'.")
    
    def search_by_tag(self, tag):
        """Search for blog posts by tag."""
        if tag in self.tags_cache:
            post_ids = self.tags_cache[tag]
            print(f"Posts for tag '{tag}': {post_ids}")
            for post_id in post_ids:
                self.view_blog_post(post_id)
        else:
            print(f"No posts found for tag '{tag}'.")
    
    def view_blog_post(self, post_id):
        """View a blog post."""
        if post_id in self.blog_posts_cache:
            post_data = self.blog_posts_cache[post_id]
            print(f"Post Title: {post_data['title']}\nContent: {post_data['content']}")
            
            # Display comments if available
            if post_id in self.comments_cache:
                print("\nComments:")
                for comment in self.comments_cache[post_id]:
                    print(f"User {comment['user_id']} said: {comment['content']} at {comment['timestamp']}")
            else:
                print("No comments yet.")
        else:
            print(f"Post '{post_id}' not found.")
    
    def authenticate_user(self, session_id):
        """Authenticate the user based on session."""
        if session_id in self.user_sessions_cache:
            session_data = self.user_sessions_cache[session_id]
            print(f"User {session_data['user_id']} logged in as {session_data['user_role']}.")
            return True
        else:
            print("Invalid session ID.")
            return False
    
    def create_user_session(self, session_id, user_id, user_role):
        """Create a user session and store it in the user_sessions_cache."""
        session_data = {
            "user_id": user_id, 
            "user_role": user_role, 
            "session_start": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.user_sessions_cache[session_id] = session_data
        print(f"User session for user {user_id} created.")

# Initialize BlogManagementSystem and simulate actions
bms = BlogManagementSystem()

# Creating user sessions
bms.create_user_session("session_abc123", 101, "admin")
bms.create_user_session("session_xyz456", 102, "author")

# Authenticating users
bms.authenticate_user("session_abc123")  # Admin login
bms.authenticate_user("session_xyz456")  # Author login

# Creating blog posts
bms.create_blog_post("post_1", "How to Learn Python", "This is the content for Python learning.", ["python", "programming"], 101)
bms.create_blog_post("post_2", "Introduction to Machine Learning", "Content about Machine Learning.", ["ML", "AI"], 102)

# Adding comments to blog posts
bms.add_comment("post_1", 1, 101, "Great post!")
bms.add_comment("post_1", 2, 103, "Very helpful, thanks!")

# Searching for blog posts by tag
bms.search_by_tag("python")  # Should show post_1
bms.search_by_tag("AI")  # Should show post_2

# Viewing blog posts
bms.view_blog_post("post_1")
bms.view_blog_post("post_2")
