CFLAGS= -Wall -g

ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

%.o: %.c
	gcc $(CFLAGS) $^ -o $@ 
	for testfile in $(wildcard *.in); do\
	     ./$@ < $$testfile ; \
       	done
	rm $@

%.samples:
	rm -f *.in *.ans
	wget https://open.kattis.com/problems/$(basename $@)/file/statement/samples.zip
	unzip samples.zip
	rm samples.zip	
	
%.test: %.c
	gcc $(CFLAGS) $^ -o $(basename $^) 
	for testfile in $(wildcard *.in); do\
	     ./$(basename $^) < $$testfile > $${testfile%.*}.guess; \
	     diff $${testfile%.*}.guess $${testfile%.*}.ans; \
	done
	rm $(basename $^)

%.submit: %.c
	python3 $(ROOT_DIR)/helpers/submit.py $^

%.clean: clean
	rm $(basename $@)

clean: $(wildcard *.guess)
	rm $? -f
	rm *.in *.ans


	
	
	 



