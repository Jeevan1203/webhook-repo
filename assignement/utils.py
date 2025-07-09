def parse_event(event_type, payload):
    if event_type == "push":
        return {
            "type": "PUSH",
            "user": payload["pusher"]["name"],
            "branch": payload["ref"].split("/")[-1]
        }

    elif event_type == "pull_request":
        user = payload["sender"]["login"]
        src_branch = payload["pull_request"]["head"]["ref"]
        dest_branch = payload["pull_request"]["base"]["ref"]

        if payload["action"] == "opened":
            return {
                "type": "PULL_REQUEST",
                "user": user,
                "source_branch": src_branch,
                "target_branch": dest_branch
            }

        elif payload["action"] == "closed" and payload["pull_request"].get("merged"):
            return {
                "type": "MERGE",
                "user": user,
                "source_branch": src_branch,
                "target_branch": dest_branch
            }

    return None
