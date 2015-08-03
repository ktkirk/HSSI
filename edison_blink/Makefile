

all: edison_blink

go-386:
	cd $(GOROOT)/src && GOOS=linux GOARCH=386 ./make.bash --no-clean

edison_blink: edison_blink.go
    #GOARCH=386 GOOS=linux go get
	GOARCH=386 GOOS=linux go build $<

put:
	scp edison_blink root@edison.local:.
