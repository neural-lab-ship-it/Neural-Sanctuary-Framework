from engine.router import Router

def main():
    router = Router(config_path="config/routing_policy.json")
    router.dry_run()

if __name__ == "__main__":
    main()
