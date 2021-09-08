CFLAGS= -Wall -g

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
	__file:= $(abspath $(lastword $(MAKEFILE_LIST)))
	__file_dir := $(dir $(mkfile_path)) # absolute path to the dir containing this makefile
	python3 __file_dir/helpers/submit.py $^


clean: $(wildcard *.guess)
	rm $? -f
	rm *.in *.ans


	
	
	 



