class Pracklr:
    def avail_lx_prog():
        avail_lx = r"""
        1. od_or_no()
        
        2. ten_comm()
        
        3. mail()
        
        4. search_patt()
        
        5. cpyfile_syscall()
        
        6. scan_dir()
        
        7. exec_fam()
        
        8. child_fork()
        
        9. wait_fork()
        
        10. signal_sigalam()
        
        11. signal_sigint()
        
        12. pipe_popen_pclose()
        
        13. read_pipe()
        
        14. cal_ser_ipc()
        
        15. prod_con()
        
        16. msg_queue()
        
        """
        return avail_lx
    def od_or_no():
        od = r"""
	echo "Enter the filename:"
	read fname
	echo "____________________"
	if [ -a $fname ]
	then
	echo "File exist"
	echo "___________________"
	if [ -f $fname ]
	then
	echo "File is an ordinary file"
	echo "_______________________"
	echo "Content of the file is:"
	echo "______________________"
	if [ -r $fname ]
	then
	cat $fname
	echo "______________________"
	fi
	if [ -w $fname ]
	then
	echo "Update the file"
	cat>> $fname
	fi
	echo "_______________________"
	echo "Updated file content is :"
	cat $fname
	else
	echo "File is not ordinary file"
	fi
	else
	echo "file is not exist"
	fi
        
        """
        return od
        
    def ten_comm():
        ten = r""" 
	z=1
	while [ $z -eq 1 ]
	do
	echo "1 - PWD"
	echo "2 - Date"
	echo "3 - Who"
	echo "4 - WhoAmI"
	echo "5 - Cal"
	echo "6 - ls"
	echo "7 - ls -i"
	echo "8 - ls -a"
	echo "9 - ls -r"
	echo "10 -ls -R"
	echo "Enter your option : "
	read x
	case $x in
	"1")pwd;;
	"2")date;;
	"3")who;;
	"4")whoami;;
	"5")cal;;
	"6")ls;;
	"7")ls -i;;
	"8")ls -a;;
	"9")ls -r;;
	"10")ls -R;;
	*) echo "Invalid Input";;
	esac
	z=0
	echo "Press 1 to Continue, 2 to Quit"
	read c
	z=$c
	done
	
	version 2
	
	z=1
	while [ $z -eq 1 ]
	do
	echo "1 - PWD"
	echo "2 - Date"
	echo "3 - Who"
	echo "4 - WhoAmI"
	echo "5 - Cal"
	echo "6 - ls"
	echo "7 - ls -i"
	echo "8 - ls -a"
	echo "9 - ls -r"
	echo "10 -ls -R"
	echo "11 -word count"
	echo "Enter your option : "
	read x
	case $x in
	"1")pwd;;
	"2")date;;
	"3")who;;
	"4")whoami;;
	"5")cal;;
	"6")ls;;
	"7")ls -i;;
	"8")ls -a;;
	"9")ls -r;;
	"10")ls -R;;
	"11")echo "Enter file name: "
	read d
	echo "No of lines"
	wc -l $d
	echo "No of words"
	wc -w $d;;
	*) echo "Invalid Input";;
	esac
	z=0
	echo "Press 1 to Continue, 2 to Quit"
	read c
	z=$c
	done
        """
        return ten
    def mail():
       ma = r"""
	s = $1
	b = $2
	echo $s $b
	shift
	shift
	for i in $*
	do
	mail -s $s $b $i
	echo “Mail successfully sent to `$i` at `date`”;
	done
       """
       return ma
       
    def search_patt():
       ser = r""" 
	echo "Argument1: $1"
	echo "Argument2: $2"
	echo "Argument3: $3"
	echo "Argument4: $4"
	echo "Argument5: $5"
	echo "Argument6: $6"
	if [ $# -eq 6 ]
	then
	echo "Program received with sufficient argument"
	for a in $1 $2 $3 $4 $5
	do
	grep -c "$6" $a
	grep -v "$6" $a
	done
	fi
	
	version 2
	
	echo "Argument 1 : $1"
	echo "Argument 2 : $2"
	echo "Argument 3 : $3"
	echo "Argument 4 : $4"
	echo "Argument 5 : $5"
	echo "Argument 6 : $6"
	if [ $# -eq 6 ]
	then
	echo "All arg received"
	fi 
	for a in $1 $2 $3 $4 $5 
	do 
	 echo "$a:`grep -c "$6" $a`"
	 echo "-------"
	done
	for a in $1 $2 $3 $4 $5
	do 
	 echo "$a"
	 echo "*****"
	 grep -r "$6" $a
	 echo "----------"
	done
       """
       return ser
    def cpyfile_syscall():
        cp = r""" 
	#include<unistd.h>
	#include<sys/stat.h>
	#include<fcntl.h>
	#include<stdio.h>
	#include<stdlib.h>
	#include<string.h>
	int main()
	{
	char c,file1[10],file2[10],text[10];
	int filein,in,out;
	printf("\nfile1 name : ");
	scanf("%s",file1);
	filein=open(file1,O_WRONLY|O_CREAT,S_IRUSR|S_IWUSR);
	printf("\nEnter some text : ");
	scanf("%s",text);
	write(filein,text,strlen(text));
	printf("\nfile2 name : ");
	scanf("%s",file2);
	close(filein);
	in=open(file1,O_RDONLY);
	out=open(file2,O_WRONLY|O_CREAT,S_IRUSR|S_IWUSR);
	while(read(in,&c,1)==1) {
	write(out,&c,1); }
	exit(0);
	}
	
	version 2
	
	#include<stdio.h>
	#include<stdlib.h>
	#include<fcntl.h>
	#include<unistd.h>
	#define BUFFER_SIZE 1024
	int main()
	{
	char input_file[100],output_file[100];
	int fd_input, fd_output,nread;
	char buffer[BUFFER_SIZE];
	printf("Enter the name of input file: ");
	scanf("%s",input_file);
	printf("Enter name of output file: ");
	scanf("%s",output_file);
	fd_input=open(input_file,O_RDONLY);
	if(fd_input == -1)
	{
	printf("Error:unable to open output file.\n");
	exit(1);
	}
	fd_output=open(output_file,O_CREAT | O_WRONLY | O_TRUNC,0644);
	if(fd_output==-1)
	{
	printf("Error:unable to open output file.\n");
	exit(1);
	}
	while((nread=read(fd_input,buffer,BUFFER_SIZE))>0)
	{
	if(write(fd_output,buffer,nread)!=nread)
	{
	printf("Error:unable to open output file.\n");
	exit(1);
	}
	}
	close(fd_input);
	close(fd_output);
	printf("File copy successful.\n");
	return 0;
	}
        """
        return cp
        
    def scan_dir():
          sc = r""" 
		#include<unistd.h>
		#include<stdio.h>
		#include<dirent.h>
		#include<string.h>
		#include<sys/stat.h>
		#include<stdlib.h>
		void scan(char *dr,int depth)
		{
		DIR *dp;
		struct dirent *insert;
		struct stat statbuf;
		if((dp=opendir(dr))==NULL)
		{
		fprintf(stderr,"Cannot open directory:%s\n",dr);
		return;
		}
		chdir(dr);
		while((insert=readdir(dp))!=NULL)
		{
		lstat(insert->d_name,&statbuf);
		if(S_ISDIR(statbuf.st_mode))
		{
		if(strcmp(".",insert->d_name)==0||strcmp("..",insert->d_name)==0)
		continue;
		printf("%*s%s/\n",depth,"",insert->d_name);
		scan(insert->d_name,depth+4);
		}
		else
		printf("%*s%s\n",depth,"",insert->d_name);
		}
		chdir("..");
		closedir(dp);
		}
		int main()
		{
		char dirname[20];
		printf("Enter a directory name for scanning : ");
		scanf("%s",dirname);
		scan(dirname,0);
		printf("Done.\n");
		exit(0);
		}
		
		version 2
		
		#include<unistd.h>
		#include<stdio.h>
		#include<dirent.h>
		#include<string.h>
		#include<sys/stat.h>
		#include<stdlib.h>
		void scan(char *dr,int depth)
		{
		DIR *dp;
		struct dirent *insert;
		struct stat statbuf;
		if((dp=opendir(dr))==NULL)
		{
		fprintf(stderr,"Cannot open directory:%s\n",dr);
		return;
		}
		chdir(dr);
		while((insert=readdir(dp))!=NULL)
		{
		lstat(insert->d_name,&statbuf);
		if(S_ISDIR(statbuf.st_mode))
		{
		if(strcmp(".",insert->d_name)==0||strcmp("..",insert->d_name)==0)
		continue;
		printf("%*s%s/\n",depth,"",insert->d_name);
		scan(insert->d_name,depth+4);
		}
		else
		printf("%*s%s\n",depth,"",insert->d_name);
		}
		chdir("..");
		closedir(dp);
		}
		int main()
		{
		char dirname[20];
		printf("Enter a directory name for scanning : ");
		scanf("%s",dirname);
		scan(dirname,0);
		printf("Done.\n");
		exit(0);
		}
     
         """
          return sc
         
    def exec_fam():
          ex_fam = r""" 
		#include<unistd.h>
		#include<stdio.h>
		#include<stdlib.h>
		int main()
		{
		char *const ps_argv[]={"ps","ax",0};
		char *const ps_envp[]={"PATH=/bin:/user/bin","TERM=console",0};
		int ch;
		printf("\n 1. running ps with execl files");
		printf("\n 2. running ps with execlp files");
		printf("\n 3. running ps with execle files");
		printf("\n 4. running ps with execv files");
		printf("\n 5. running ps with execvp files");
		printf("\n 6. running ps with execve files");
		printf("\n Enter your choice:");
		scanf("%d",&ch);
		switch(ch)
		{
		case 1:
		printf("Running ps with execl files \n");
		execl("/bin/ps","ps","ax",0);
		printf("done");
		break;
		case 2:
		printf("Running ps with execlp files \n");
		execlp("ps","ps","ax",0);
		printf("done");
		break;
		case 3:
		printf("Running ps with execle files \n");
		execle("/bin/ps","ps","ax",0,ps_envp);
		printf("done");
		break;
		case 4:
		printf("Running ps with execv files \n");
		execv("/bin/ps",ps_argv);
		printf("done");
		break;case 5:
		printf("Running ps with execvp files \n");
		execvp("ps",ps_argv);
		printf("done");
		break;
		case 6:
		printf("Running ps with execve files \n");
		execve("/bin/ps",ps_argv,ps_envp);
		printf("done");
		break;
		default:
		printf("invalid choice..\n");
		break;
		}
		exit(0);
		}
		
		version 2
		
		#include<unistd.h>
		#include<stdio.h>
		#include<stdlib.h>
		int main()
		{
		char *const ps_argv[]={"ps","ax",0};
		char *const ps_envp[]={"PATH=/bin:/user/bin","TERM=console",0};
		int ch;
		printf("\n 1. running ps with execl files");
		printf("\n 2. running ps with execlp files");
		printf("\n 3. running ps with execle files");
		printf("\n 4. running ps with execv files");
		printf("\n 5. running ps with execvp files");
		printf("\n 6. running ps with execve files");
		printf("\n Enter your choice:");
		scanf("%d",&ch);
		switch(ch)
		{
		case 1:
		printf("Running ps with execl files \n");
		execl("/bin/ps","ps","ax",0);
		printf("done");
		break;
		case 2:
		printf("Running ps with execlp files \n");
		execlp("ps","ps","ax",0);
		printf("done");
		break;
		case 3:
		printf("Running ps with execle files \n");
		execle("/bin/ps","ps","ax",0,ps_envp);
		printf("done");
		break;
		case 4:
		printf("Running ps with execv files \n");
		execv("/bin/ps",ps_argv);
		printf("done");
		break;
		case 5:
		printf("Running ps with execvp files \n");
		execvp("ps",ps_argv);
		printf("done");
		break;
		case 6:
		printf("Running ps with execve files \n");
		execve("/bin/ps",ps_argv,ps_envp);
		printf("done");
		break;
		default:
		printf("invalid choice..\n");
		break;
		}
		exit(0);
		}
          
          """
          return ex_fam   
    def child_fork():
          cld = r""" 
		#include<sys/types.h>
		#include<unistd.h>
		#include<stdio.h>
		#include<stdlib.h>
		int main()
		{
		pid_t pid;
		char * message;
		int n;
		printf("fork program starting \n");
		pid=fork();
		switch(pid)
		{
		case - 1:
		perror("fork failed");
		exit(1);
		case 0:
		message="this is the child";
		n=5;
		break;
		default:
		message="this is the parent";
		n=3;
		break;
		}
		for(;n>0;n--)
		{
		puts(message);
		sleep(1);
		}
		exit(0);
		}
		
		version 2
		
		#include<sys/types.h>
		#include<unistd.h>
		#include<stdio.h> 
		#include<stdlib.h>
		int main()
		{ 
		pid_t pid; 
		char* message; 
		int n;
		printf("fork program starting \n"); 
		pid=fork(); 
		switch(pid)
		{
		case - 1:
		perror("fork failed");
		exit(1);
		case 0:
		message="this is the child";
		n=5;
		break;
		default:
		message="this is the parent";
		n=3;
		break;
		} 
		for(;n>0;n--)
		{
		puts(message);
		sleep(1);
		}
		exit(0);
		}
		
		version 3 using pipes
		
		#include<stdio.h>
		#include<unistd.h>

		int main() {
		   int pipefds[2];
		   int returnstatus;
		   int pid;
		   char writemessages[2][20]={"Hi", "Hello"};
		   char readmessage[20];
		   returnstatus = pipe(pipefds);
		   if (returnstatus == -1) {
		      printf("Unable to create pipe\n");
		      return 1;
		   }
		   pid = fork();
		   
		   // Child process
		   if (pid == 0) {
		      read(pipefds[0], readmessage, sizeof(readmessage));
		      printf("Child Process - Reading from pipe – Message 1 is %s\n", readmessage);
		      read(pipefds[0], readmessage, sizeof(readmessage));
		      printf("Child Process - Reading from pipe – Message 2 is %s\n", readmessage);
		   } else { //Parent process
		      printf("Parent Process - Writing to pipe - Message 1 is %s\n", writemessages[0]);
		      write(pipefds[1], writemessages[0], sizeof(writemessages[0]));
		      printf("Parent Process - Writing to pipe - Message 2 is %s\n", writemessages[1]);
		      write(pipefds[1], writemessages[1], sizeof(writemessages[1]));
		   }
		   return 0;
		}
          """
          return cld
    
    def wait_fork():
          waitf = r"""  
		#include <sys/types.h>
		#include <sys/wait.h>
		#include <unistd.h>
		#include <stdio.h>
		#include <stdlib.h>
		int main()
		{
		pid_t pid;
		char *msg;
		int n;
		int exit_code;
		printf("Fork program starting\n");
		pid=fork();
		switch(pid)
		{
		case -1:
		perror("fork failed");
		exit(1);
		case 0:
		msg = "this is child";
		n = 5;
		exit_code = 37;
		break;
		default:
		msg = "this is parent";
		n = 3;
		exit_code = 0;
		break;
		}
		for(; n>0;n--)
		{
		puts(msg);
		sleep(1);
		}if(pid !=0)
		{
		int stat_val;
		pid_t
		child_pid;
		child_pid = wait(&stat_val);
		printf("child has finished: PID = %d\n", child_pid);
		if(WIFEXITED(stat_val))
		printf("child exited code %d\n", WEXITSTATUS(stat_val));
		else
		printf("child terminated abnormally\n");
		}
		exit(exit_code);
		}
		
		version 2
		
		#include <sys/types.h>
		#include <sys/wait.h>
		#include <unistd.h>
		#include <stdio.h>
		#include <stdlib.h>
		int main()
		{
		pid_t pid;
		char *msg;
		int n;
		int exit_code;
		printf("Fork program starting\n");
		pid=fork();
		switch(pid)
		{
		case -1:
		perror("fork failed");
		exit(1);
		case 0:
		msg = "this is child";
		n = 5;
		exit_code = 37;
		break;
		default:
		msg = "this is parent";
		n = 3;
		exit_code = 0;
		break;
		}
		for(; n>0;n--)
		{
		puts(msg);
		sleep(1);
		}
		if(pid !=0)
		{
		int stat_val;
		pid_t
		child_pid;
		child_pid = wait(&stat_val);
		printf("child has finished: PID = %d\n", child_pid);
		if(WIFEXITED(stat_val))
		printf("child exited code %d\n", WEXITSTATUS(stat_val));
		else
		printf("child terminated abnormally\n");
		}
		exit(exit_code);
		}

          
          """
          return waitf      
    def signal_sigalam():
          sig_lam = r"""           
		#include<sys/types.h>
		#include<unistd.h>
		#include<signal.h>
		#include<stdio.h>
		#include<stdlib.h>
		static int alarm_fired=0;
		void ding(int sig)
		{
		alarm_fired=1;
		}
		int main()
		{
		pid_t pid;
		printf("Alarm application starting\n");
		pid=fork();
		switch(pid)
		{
		case -1:
		printf("Fork failed");
		exit(1);
		case 0:
		sleep(1);
		kill(getppid(),SIGALRM);
		exit(0);
		}
		printf("Waiting for alarm to go off\n");
		(void) signal(SIGALRM,ding);
		pause();
		if(alarm_fired)
		printf("Ding\n");
		printf("Done\n");
		exit(0);
		}
		
		version 2
		
		#include<unistd.h>
		#include<signal.h>
		#include<stdio.h>
		#include<stdlib.h>
		static int alarm_fired=0;
		void ding(int sig)
		{
		alarm_fired=1;
		}
		int main()
		{
		pid_t pid;
		printf("Alarm application starting\n");
		pid=fork();
		switch(pid)
		{
		case -1:
		printf("Fork failed");
		exit(1);
		case 0:
		sleep(1);
		kill(getppid(),SIGALRM);
		exit(0);
		}
		printf("Waiting for alarm to go off\n");
		(void) signal(SIGALRM,ding);
		pause();
		if(alarm_fired)
		printf("Ding\n");
		printf("Done\n");
		exit(0);
		}
          """
          return sig_lam   
    def signal_sigint():
          sig_int = r""" 
		#include<signal.h>
		#include<stdio.h>
		#include<unistd.h>
		void ouch(int sig)
		{
		printf("OUCH! -I got signal %d\n",sig);
		(void)signal(SIGINT,SIG_DFL);
		}
		int main()
		{
		(void)signal(SIGINT,ouch);
		while(1)
		{
		printf("hello world!\n");
		sleep(1);
		}
		}
		
		version 2 using shell
		
		run.sh
		
		#!/bin/bash

		gcc -o program program.c
		./program
		
		program.c
		
		#include<signal.h>
		#include<stdio.h>
		#include<unistd.h>
		void ouch(int sig)
		{
		printf("OUCH! -I got signal %d\n",sig);
		(void)signal(SIGINT,SIG_DFL);
		}
		int main()
		{
		(void)signal(SIGINT,ouch);
		while(1)
		{
		printf("hello world!\n");
		sleep(1);
		}
		}
		
          
          """
          return sig_int
    def pipe_popen_pclose():
          pipe_po_pc = r"""
		#include<unistd.h>
		#include<stdlib.h>
		#include<stdio.h>
		#include<string.h>
		int main()
		{
		int data_processed;
		int file_pipes[2];
		const char some_data[]="BHARATHIAR UNIVERSITY-COMPUTER SCIENCE";
		char buffer[BUFSIZ+1];
		memset(buffer,'\0',sizeof(buffer));
		if(pipe(file_pipes)==0)
		{
		data_processed=write(file_pipes[1],some_data,strlen(some_data));
		printf("Wrote %d bytes\n",data_processed);
		data_processed=read(file_pipes[0],buffer,BUFSIZ);
		printf("Read %d bytes: %s\n",data_processed,buffer);
		exit(EXIT_SUCCESS);
		}
		exit(EXIT_FAILURE);
		}
		
          """
          return pipe_po_pc
          
    def read_pipe():
          rd_pip = r"""
		#include<unistd.h>
		#include<stdlib.h>
		#include<stdio.h>
		#include<string.h>
		int main()
		{
		FILE *read_fp;
		char buffer[BUFSIZ +1];
		int chars_read;
		memset(buffer,'\0',sizeof(buffer));
		read_fp = popen("ps ax","r");
		if(read_fp !=NULL) {
		chars_read=fread(buffer,sizeof(char),BUFSIZ,read_fp);
		printf("%d",chars_read);
		while(chars_read > 0)
		{
		buffer[chars_read - 1]='\0';
		printf("reading %d:-\n %s\n",BUFSIZ,buffer);
		chars_read=fread(buffer,sizeof(char),BUFSIZ,read_fp);
		}
		pclose(read_fp);
		exit(EXIT_SUCCESS); }
		exit(EXIT_FAILURE);
		}
		
		version 2
		
		#include<unistd.h>
		#include<stdlib.h>
		#include<stdio.h>
		#include<string.h>
		int main()
		{
		FILE *read_fp;
		char buffer[BUFSIZ +1];
		int chars_read;
		memset(buffer,'\0',sizeof(buffer));
		read_fp = popen("ps ax","r");
		if(read_fp !=NULL) {
		chars_read=fread(buffer,sizeof(char),BUFSIZ,read_fp);
		printf("%d",chars_read);
		while(chars_read > 0)
		{
		buffer[chars_read - 1]='\0';
		printf("reading %d:-\n %s\n",BUFSIZ,buffer);
		chars_read=fread(buffer,sizeof(char),BUFSIZ,read_fp);
		}
		pclose(read_fp);
		exit(EXIT_SUCCESS); 
		}
		exit(EXIT_FAILURE);
		}
		
		version 3 read and write
		
		#include<stdio.h>
		#include<unistd.h>

		int main() {
		   int pipefds[2];
		   int returnstatus;
		   char writemessages[2][20]={"Hi", "Hello"};
		   char readmessage[20];
		   returnstatus = pipe(pipefds);
		   
		   if (returnstatus == -1) {
		      printf("Unable to create pipe\n");
		      return 1;
		   }
		   
		   printf("Writing to pipe - Message 1 is %s\n", writemessages[0]);
		   write(pipefds[1], writemessages[0], sizeof(writemessages[0]));
		   read(pipefds[0], readmessage, sizeof(readmessage));
		   printf("Reading from pipe – Message 1 is %s\n", readmessage);
		   printf("Writing to pipe - Message 2 is %s\n", writemessages[0]);
		   write(pipefds[1], writemessages[1], sizeof(writemessages[0]));
		   read(pipefds[0], readmessage, sizeof(readmessage));
		   printf("Reading from pipe – Message 2 is %s\n", readmessage);
		   return 0;
		}
          
          """ 
          return rd_pip  
          
    def cal_ser_ipc():
          cal_ser = r""" 
		client.h

		#include<unistd.h>
		#include<stdlib.h>
		#include<stdio.h>
		#include<string.h>
		#include<fcntl.h>
		#include<limits.h>
		#include<sys/types.h>
		#include<sys/stat.h>
		#define SERVER_FIFO_NAME "/tmp/serv_fifo"
		#define CLIENT_FIFO_NAME "/tmp/cli_%d_fifo"
		#define BUFFER_SIZE 20
		struct data_to_pass_st
		{
		pid_t client_pid;
		char some_data[BUFFER_SIZE-1];
		};

		client.c

		#include "client.h"
		#include<ctype.h>
		int main()
		{
		int server_fifo_fd,client_fifo_fd;
		struct data_to_pass_st my_data;
		int times_to_send;
		char client_fifo[256];
		server_fifo_fd=open(SERVER_FIFO_NAME,O_WRONLY);
		if(server_fifo_fd==-1) {
		fprintf(stderr,"Sorry, no server\n");
		exit(EXIT_FAILURE); }
		my_data.client_pid=getpid();
		sprintf(client_fifo, CLIENT_FIFO_NAME, my_data.client_pid);
		if(mkfifo(client_fifo,0777)==-1) {
		fprintf(stderr,"Sorry,cannot make %s\n",client_fifo);
		exit(EXIT_FAILURE); }
		for(times_to_send=0;times_to_send<2;times_to_send++) {
		sprintf(my_data.some_data,"welcome %d",my_data.client_pid);
		printf("%d sent %s,",my_data.client_pid,my_data.some_data);
		write(server_fifo_fd,&my_data,sizeof(my_data));
		client_fifo_fd=open(client_fifo,O_RDONLY);
		if(client_fifo_fd!=-1) {
		if(read(client_fifo_fd,&my_data,sizeof(my_data))>0)
		{
		printf("received: %s\n",my_data.some_data);
		}
		close(client_fifo_fd);
		}
		}
		close(server_fifo_fd);
		unlink(client_fifo);
		exit(EXIT_SUCCESS);
		}

		server.c

		#include "client.h"
		#include<ctype.h>
		int main()
		{
		int server_fifo_fd,client_fifo_fd;
		struct data_to_pass_st my_data;
		int read_res;
		char client_fifo[256];
		char *tmp_char_ptr;
		mkfifo(SERVER_FIFO_NAME,0777);
		server_fifo_fd=open(SERVER_FIFO_NAME,O_RDONLY);
		if(server_fifo_fd==-1)
		{
		fprintf(stderr,"Server fifo failure\n");
		exit(EXIT_FAILURE);
		}
		sleep(2);
		do
		{
		read_res=read(server_fifo_fd,&my_data,sizeof(my_data));
		if(read_res>0)
		{
		tmp_char_ptr=my_data.some_data;
		while(*tmp_char_ptr)
		{
		*tmp_char_ptr=toupper(*tmp_char_ptr);
		tmp_char_ptr++;
		}
		sprintf(client_fifo,CLIENT_FIFO_NAME,my_data.client_pid);
		client_fifo_fd=open(client_fifo,O_WRONLY);
		if(client_fifo_fd!=-1)
		{
		write(client_fifo_fd,&my_data,sizeof(my_data));
		close(client_fifo_fd);
		}
		}
		}
		while(read_res>0);
		close(server_fifo_fd);
		unlink(SERVER_FIFO_NAME);
		exit(EXIT_SUCCESS);
		}
		
		version 2
		
		Client.h
		
		#include<unistd.h>
		#include<stdlib.h>
		#include<stdio.h>
		#include<string.h>
		#include<fcntl.h>
		#include<limits.h>
		#include<sys/types.h>
		#include<sys/stat.h>
		#define SERVER_FIFO_NAME "/tmp/serv_fifo"
		#define CLIENT_FIFO_NAME "/tmp/cli_%d_fifo"
		#define BUFFER_SIZE 20
		struct data_to_pass_st
		{
		pid_t client_pid;
		char some_data[BUFFER_SIZE-1];
		};
		
		Server Program:
		
		#include "client.h"
		#include<ctype.h>
		int main()
		{
		int server_fifo_fd,client_fifo_fd;
		struct data_to_pass_st my_data;
		int read_res;
		char client_fifo[256];char *tmp_char_ptr;
		mkfifo(SERVER_FIFO_NAME,0777);
		server_fifo_fd=open(SERVER_FIFO_NAME,O_RDONLY);
		if(server_fifo_fd==-1)
		{
		fprintf(stderr,"Server fifo failure\n");
		exit(EXIT_FAILURE);
		}
		sleep(2);
		do
		{
		read_res=read(server_fifo_fd,&my_data,sizeof(my_data));
		if(read_res>0)
		{
		tmp_char_ptr=my_data.some_data;
		while(*tmp_char_ptr)
		{
		*tmp_char_ptr=toupper(*tmp_char_ptr);
		tmp_char_ptr++;
		}
		sprintf(client_fifo,CLIENT_FIFO_NAME,my_data.client_pid);
		client_fifo_fd=open(client_fifo,O_WRONLY);
		if(client_fifo_fd!=-1)
		{
		write(client_fifo_fd,&my_data,sizeof(my_data));
		close(client_fifo_fd);
		}
		}
		}while(read_res>0);
		close(server_fifo_fd);
		unlink(SERVER_FIFO_NAME);
		exit(EXIT_SUCCESS);
		}
		
		Client Program:
		
		
		#include "client.h"
		#include<ctype.h>
		int main()
		{
		int server_fifo_fd,client_fifo_fd;
		struct data_to_pass_st my_data;
		int times_to_send;
		char client_fifo[256];
		server_fifo_fd=open(SERVER_FIFO_NAME,O_WRONLY);
		if(server_fifo_fd==-1) {
		fprintf(stderr,"Sorry, no server\n");
		exit(EXIT_FAILURE); }
		my_data.client_pid=getpid();
		sprintf(client_fifo, CLIENT_FIFO_NAME, my_data.client_pid);
		if(mkfifo(client_fifo,0777)==-1) {
		fprintf(stderr,"Sorry,canâ€™t make %s\n",client_fifo);
		exit(EXIT_FAILURE); }
		for(times_to_send=0;times_to_send<2;times_to_send++) {
		sprintf(my_data.some_data,"welcome %d",my_data.client_pid);
		printf("%d sent %s,",my_data.client_pid,my_data.some_data);
		write(server_fifo_fd,&my_data,sizeof(my_data));
		client_fifo_fd=open(client_fifo,O_RDONLY);
		if(client_fifo_fd!=-1) {if(read(client_fifo_fd,&my_data,sizeof(my_data))>0)
		{
		printf("received: %s\n",my_data.some_data);
		}
		close(client_fifo_fd);
		}
		}
		close(server_fifo_fd);
		unlink(client_fifo);
		exit(EXIT_SUCCESS);
		}

          
          """
          return cal_ser 
    def prod_con():
          prod = r""" 
          
               pro.c
		
		#include<stdio.h>
		#include<stdlib.h>
		#include<unistd.h>
		#include<sys/shm.h>
		#include<string.h>
		int main()
		{
		int i;
		void *shared_memory;
		char buff[100];
		int shmid;
		shmid=shmget((key_t)2345, 1024, 0666|IPC_CREAT);
		printf("Key of shared memory is %d\n",shmid);
		shared_memory=shmat(shmid,NULL,0); //process attached to shared memory segment
		printf("Process attached at %p\n",shared_memory); //this prints the address where the segment is attached with this process
		printf("Enter some data to write to shared memory\n");
		read(0,buff,100); //get some input from user
		strcpy(shared_memory,buff); //data written to shared memory
		printf("You wrote : %s\n",(char *)shared_memory);
		}
		
		con.c
		
		#include<stdio.h>
		#include<stdlib.h>
		#include<unistd.h>
		#include<sys/shm.h>
		#include<string.h>
		int main()
		{
		int i;
		void *shared_memory;
		char buff[100];
		int shmid;
		shmid=shmget((key_t)2345, 1024, 0666);
		printf("Key of shared memory is %d\n",shmid);
		shared_memory=shmat(shmid,NULL,0); //process attached to shared memory segment
		printf("Process attached at %p\n",shared_memory);
		printf("Data read from shared memory is : %s\n",(char *)shared_memory);
		}
		
		version 2
		
		shm-com.h
		#define TEXT_SZ 2048
		struct shared_use_st
		{
		int written_by_you;
		char some_text[TEXT_SZ];
		};
		Consumer Program:
		#include<unistd.h>
		#include<stdlib.h>
		#include<stdio.h>
		#include<string.h>
		#include<sys/shm.h>
		#include "shm-com.h"
		int main()
		{
		int running=1;
		void *shared_memory=(void *)0;
		struct shared_use_st *shared_stuff;
		int shmid;
		srand((unsigned int)getpid());
		shmid=shmget((key_t)1234,sizeof(struct shared_use_st),0666|IPC_CREAT);shared_memory=shmat(shmid,(void *)0,0);
		printf("Memory attached at %X\n",(int)shared_memory);
		shared_stuff=(struct shared_use_st *)shared_memory;
		shared_stuff->written_by_you=0;
		while(running)
		{
		if(shared_stuff->written_by_you)
		{
		printf("You wrote: %s",shared_stuff->some_text);
		sleep(rand()%1);
		shared_stuff->written_by_you=0;
		if(strncmp(shared_stuff->some_text,"end",3)==0)
		{
		running=0;
		}
		}
		}
		if(shmdt(shared_memory)==0)
		{
		printf("success\n");
		exit(EXIT_FAILURE);
		}
		if(shmctl(shmid,IPC_RMID,0)==-1)
		{fprintf(stderr,"shmctl(IPC_RMID) failed\n");
		exit(EXIT_FAILURE);
		}
		exit(EXIT_SUCCESS);
		}
		Producer Program:
		#include<unistd.h>
		#include<stdlib.h>
		#include<stdio.h>
		#include<string.h>
		#include<sys/shm.h>
		#include "shm-com.h"
		int main()
		{
		int running=1;
		void *shared_memory=(void *)0;
		struct shared_use_st *shared_stuff;
		char buffer[BUFSIZ];
		int shmid;
		shmid=shmget((key_t)1234,sizeof(struct shared_use_st),0666|IPC_CREAT);
		shared_memory=shmat(shmid,(void *)0,0);
		printf("Memory attached at %X\n",(int)shared_memory);
		shared_stuff=(struct shared_use_st *)shared_memory;
		while(running){
		while(shared_stuff->written_by_you==1)
		{
		sleep(1);
		printf("wait\n");
		}
		printf("Enter some text : ");
		fgets(buffer,BUFSIZ,stdin);
		strncpy(shared_stuff->some_text,buffer,TEXT_SZ);
		shared_stuff->written_by_you=1;
		if(strncmp(buffer,"end",3)==0)
		{
		running=0;
		}
		}
		if(shmdt(shared_memory)==0)
		{
		printf("success\n");
		exit(EXIT_FAILURE);
		exit(EXIT_SUCCESS);
		}
          """
          return prod
    def msg_queue(): 
         msg_q = r""" 
         sender.c
         
         #include<stdlib.h>
	 #include<stdio.h>
	 #include<string.h>
	 #include<unistd.h>
	 #include<sys/types.h>
	 #include<sys/ipc.h>
	 #include<sys/msg.h>
	 #define MAX_TEXT 512   //maximum length of the message that can be sent allowed
	 struct my_msg{
		 long int msg_type;
		 char some_text[MAX_TEXT];
	 };
	 int main()
	 {
		 int running=1;
		 int msgid;
		 struct my_msg some_data;
		 char buffer[50]; //array to store user input
		 msgid=msgget((key_t)14534,0666|IPC_CREAT);
		 if (msgid == -1) // -1 means the message queue is not created
		 {
		         printf("Error in creating queue\n");
		         exit(0);
		 }

		 while(running)
		 {
		         printf("Enter some text:\n");
		         fgets(buffer,50,stdin);
		         some_data.msg_type=1;
		         strcpy(some_data.some_text,buffer);
		         if(msgsnd(msgid,(void *)&some_data, MAX_TEXT,0)==-1) // msgsnd returns -1 if the message is not sent
		         {
		                 printf("Msg not sent\n");
		         }
		         if(strncmp(buffer,"end",3)==0)
		         {
		                 running=0;
		         }
		 }
	 }
	 
	 rec.c
	 
	 #include<stdlib.h>
	 #include<stdio.h>
	 #include<string.h>
	 #include<unistd.h>
	 #include<sys/types.h>
	 #include<sys/ipc.h>
	 #include<sys/msg.h>
	 struct my_msg{
		 long int msg_type;
		 char some_text[BUFSIZ];
	 };
	 int main()
	 {
		 int running=1;
		 int msgid;
		 struct my_msg some_data;
		 long int msg_to_rec=0;
		 msgid=msgget((key_t)14534,0666|IPC_CREAT);
		 while(running)
		 {
		         msgrcv(msgid,(void *)&some_data,BUFSIZ,msg_to_rec,0);                 
		         printf("Data received: %s\n",some_data.some_text);
		         if(strncmp(some_data.some_text,"end",3)==0)
		         {
		                 running=0;
		         }
		 }
		  msgctl(msgid,IPC_RMID,0);
	 }
	 
		version 2
		 
		Message 1 program:
		#include <stdlib.h>
		#include<stdio.h>
		#include<string.h>
		#include<errno.h>
		#include<unistd.h>
		#include<sys/msg.h>
		struct my_msg_st
		{
		long int my_msg_type;
		char some_text[BUFSIZ];
		};
		int main()
		{
		int running=1;
		int msgid;
		struct my_msg_st some_data;
		long int msg_to_receive=0;
		msgid=msgget((key_t)1234,0666|IPC_CREAT);
		if(msgid==-1)
		{
		fprintf(stderr,"msgget failed with error: %d\n",errno);
		exit(EXIT_FAILURE);}
		while(running)
		{
		if(msgrcv(msgid,(void *)&some_data,BUFSIZ,msg_to_receive,0)==-1)
		{
		fprintf(stderr,"msgrcv failed with error: %d\n",errno);
		exit(EXIT_FAILURE);
		}
		printf("You wrote:%s",some_data.some_text);
		if(strncmp(some_data.some_text,"end",3)==0)
		{
		running=0;
		}
		}
		if(msgctl(msgid,IPC_RMID,0)==-1)
		{
		fprintf(stderr,"msgctl(IPC_RMID)failed\n");
		exit(EXIT_FAILURE);
		}
		exit(EXIT_SUCCESS);
		}
		Message 2 Program:
		#include<stdlib.h>
		#include<stdio.h>
		#include<string.h>
		#include<errno.h>#include<unistd.h>
		#include<sys/msg.h>
		#define MAX_TEXT 512
		struct my_msg_st
		{
		long int my_msg_type;
		char some_text[MAX_TEXT];
		};
		int main()
		{
		int running=1;
		struct my_msg_st some_data;
		int msgid;
		char buffer[BUFSIZ];
		msgid=msgget((key_t)1234,0666|IPC_CREAT);
		if(msgid==-1)
		{
		fprintf(stderr,"msgget failed with error: %d\n",errno);
		exit(EXIT_FAILURE);
		}
		while(running)
		{
		printf("Enter some text:");
		fgets(buffer,BUFSIZ,stdin);
		some_data.my_msg_type = 1;
		strcpy(some_data.some_text, buffer);if(msgsnd(msgid,(void *)&some_data,MAX_TEXT,0)==-1)
		{
		fprintf(stderr,"msgsnd failed\n");
		exit(EXIT_FAILURE);
		}
		if(strncmp(buffer,"end",3)==0)
		{
		running=0;
		}
		}
		exit(EXIT_SUCCESS);
		}
		 
         """      
         return msg_q
