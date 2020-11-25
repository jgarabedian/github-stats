from flask import Flask, render_template
from github import Github
import pprint

g = Github("714448b4008ce215bd31963c6f23ae1b2755cd81")

app = Flask(__name__)

@app.route('/')
def index():
	user = g.get_user()
	repos = g.get_user().get_repos(sort="updated", visibility="public")
	# sorted_repos = sorted(list(repos), key=lambda k: k['updated_at'], reverse=True)
	# pprint.pprint(repos[0].__dict__)
	# r_list = [vars(r) for r in repos]

	# pprint.pprint(r_list[0])
	# r_sort = sorted(r_list, key=lambda k: k['_rawData']['forks_count'])

	return render_template('index.html', user=user, details=repos)