from rx.subject import Subject

c = Subject()

c.subscribe(
    on_next= lambda i: print("on_next called with {}".format(i))
)


c.on_next("ss")