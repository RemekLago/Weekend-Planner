from app import celery

@celery.task()
def add_together():
    print("1")
    return True

if __name__ == "__main__":
    var = add_together.delay()
    print(var)
    