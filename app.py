from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)

matches = pd.read_csv("01_data/matches.csv")
deliveries = pd.read_csv("01_data/deliveries.csv")
all_teams = sorted(set(matches["team1"]).union(set(matches["team2"])))
matches_per_season = matches.groupby("season").size()

team_wins = matches["winner"].value_counts().head(10)

player_awards = matches["player_of_match"].value_counts().head(10)

top_players = player_awards.index.tolist()
top_awards = player_awards.values.tolist()

winning_teams = team_wins.index.tolist()
winning_counts = team_wins.values.tolist()

seasons = [str(x) for x in matches_per_season.index]
season_matches = [int(x) for x in matches_per_season.values]

@app.route("/")
def home():

    selected_team = request.args.get("team")
    selected_season = request.args.get("season")

    filtered_matches = matches.copy()

    # Filter by team
    if selected_team:
        filtered_matches = filtered_matches[
            (filtered_matches["team1"] == selected_team) |
            (filtered_matches["team2"] == selected_team)
        ]

    # Filter by season
    if selected_season:
        filtered_matches = filtered_matches[
            filtered_matches["season"].astype(str) == selected_season
        ]

    # Charts (always calculate after filtering)
    filtered_matches_per_season = filtered_matches.groupby("season").size()

    filtered_team_wins = filtered_matches["winner"].value_counts().head(10)

    filtered_player_awards = filtered_matches["player_of_match"].value_counts().head(10)

    filtered_venues = filtered_matches["venue"].value_counts().head(10)

    top_venues = filtered_venues.index.tolist()
    venue_matches = filtered_venues.values.tolist()

    filtered_seasons = [str(x) for x in filtered_matches_per_season.index]
    filtered_season_matches = [int(x) for x in filtered_matches_per_season.values]

    filtered_winning_teams = filtered_team_wins.index.tolist()
    filtered_winning_counts = filtered_team_wins.values.tolist()

    filtered_top_players = filtered_player_awards.index.tolist()
    filtered_top_awards = filtered_player_awards.values.tolist()

    # Cards
    total_matches = filtered_matches["match_id"].nunique()
    total_teams = len(set(filtered_matches["team1"]).union(set(filtered_matches["team2"])))
    total_seasons = filtered_matches["season"].nunique()
    total_venues = filtered_matches["venue"].nunique()
    # Top 10 Run Scorers (Orange Cap)
    top_batsmen = deliveries.groupby("batter")["batter_runs"].sum().sort_values(ascending=False).head(10)

    batsman_names = top_batsmen.index.tolist()
    batsman_runs = top_batsmen.values.tolist()

    return render_template(
    "index.html",
    total_matches=total_matches,
    total_teams=total_teams,
    total_seasons=total_seasons,
    total_venues=total_venues,
    seasons=seasons,
    season_matches=filtered_season_matches,
    winning_teams=filtered_winning_teams,
    winning_counts=filtered_winning_counts,
    top_players=filtered_top_players,
    top_awards=filtered_top_awards,
    top_venues=top_venues,
    venue_matches=venue_matches,
    all_teams=all_teams,
    batsman_names=batsman_names,
    batsman_runs=batsman_runs,
)
@app.route("/download")
def download():

    selected_team = request.args.get("team")
    selected_season = request.args.get("season")
    search = request.args.get("search")

    filtered_matches = matches.copy()

    if selected_team:
        filtered_matches = filtered_matches[
            (filtered_matches["team1"] == selected_team) |
            (filtered_matches["team2"] == selected_team)
        ]

    if selected_season:
        filtered_matches = filtered_matches[
            filtered_matches["season"].astype(str) == selected_season
        ]
    if search:
        filtered_matches = filtered_matches[
        filtered_matches["team1"].str.contains(search, case=False, na=False) |
        filtered_matches["team2"].str.contains(search, case=False, na=False) |
        filtered_matches["player_of_match"].str.contains(search, case=False, na=False)
    ]

    output = io.StringIO()
    filtered_matches.to_csv(output, index=False)

    mem = io.BytesIO()
    mem.write(output.getvalue().encode("utf-8"))
    mem.seek(0)

    return send_file(
        mem,
        mimetype="text/csv",
        as_attachment=True,
        download_name="filtered_matches.csv"
    )
if __name__ == "__main__":
    app.run(debug=True)