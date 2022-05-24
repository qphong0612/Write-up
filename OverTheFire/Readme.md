
# OverTheWire

### Level 0
Sử dụng SSH connect tới host bandit.labs.overthewire.org, port 2220 với username và password là bandi0

    ssh bandit0@bandit.labs.overthewire.org -p 2220
    ls -a1
    cat readme
![Screenshot_2021-09-22_23-47-25](https://user-images.githubusercontent.com/83420725/134452332-0d5b4b2d-232c-4205-bc01-9eeb66b2243c.png)
> Flag: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

### Level 1
     ssh bandit1@bandit.labs.overthewire.org -p 2220
Mật khẩu cho cấp độ tiếp theo được lưu trữ trong một tệp có tên '-' nằm trong thư mục chính

     cat ./-
 ![level1](https://user-images.githubusercontent.com/83420725/134464588-3f396137-8aee-494e-b800-f39d7b84b6b4.png)
> Flag: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

### Level 2
      ssh bandit2@bandit.labs.overthewire.org -p 2220
Mật khẩu cho cấp độ tiếp theo được lưu trữ trong một tệp được gọi là 'spaces in this filename' tệp này nằm trong thư mục chính

      cat 'spaces in this filename'
![level2](https://user-images.githubusercontent.com/83420725/134464597-db3e727d-2616-41ba-88d3-e00703903fa4.png)      
> Flag: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
### Level 3
      ssh bandit3@bandit.labs.overthewire.org -p 2220
Mật khẩu cho cấp độ tiếp theo được lưu trữ trong một tệp hidden trong thư mục inhere.

      cd inhere && ls -a
      cat .hidden 
![level3](https://user-images.githubusercontent.com/83420725/134464602-89a64ff2-8989-4b21-aa7d-cb2f2aab5dac.png)      
> Flag: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

### Level 4
      ssh bandit4@bandit.labs.overthewire.org -p 2220
Mật khẩu cho cấp độ tiếp theo được lưu trữ trong tệp duy nhất con người có thể đọc được trong thư mục inhere.

      cd inhere && ls -a 
      grep -E '[a-z]' -- * 
![level4](https://user-images.githubusercontent.com/83420725/134464608-c3f735c2-0d04-4260-8e08-76cb710b06a8.png)
> Flag: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

### Level 5
      ssh bandit5@bandit.labs.overthewire.org -p 2220
     
 Password được lưu trong một file trong thư mục inhere và là chuỗi con người có thể đọc được, 1033 byte, không thực thi 
        
       find . -size 1033c \! -executable
 Lệnh file trả về đường dẫn ./maybehere07/.file2 sử dụng lệnh cat để lấy được 
      
> Flag: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

### Level 6
Sử  dụng  câu  lệnh  sshpass  để truy  cập  vào level 6
       
       sshpass -p 'DXjZPULLxYr17uwoI01bNLQbtFemEgo7' ssh bandit6@bandit.labs.overthewire.org -p 2220
     
Password  cho level  tiếp theo được lưu một  nơi nào đó thuộc  sở  hữu  của  user  bandit7, thuộc  sở  hữu  group  bandit6 và  có kích thước 33 bytes.
Để  tìm  được  file  lưu password sử dụng câu lệnh find
    
        find  / -type f  -size  33c  -user  bandit7 -group  bandit6 2>/dev/null
        
Lệnh  find  trả về  path /var/lib/dpkg/info/bandit7.password, cuối  cùng  dùng  lệnh cat để lấy  pass cho level tiếp theo

        cat  /var/lib/dpkg/info/bandit7.password
> Flag: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

### Level 7
Sử  dụng  câu  lệnh  sshpass  để truy  cập  vào level 7

      sshpass  -p  'HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs' ssh bandit7@bandit.labs.overthewire.org -p 2220
      
Password  cho level  tiếp theo được lưu  trong  file  data.txt  và  bên  cạnh  từ  millionth. Trong  file  data.txt  chứa  nhiều dữ  liệu để tìm chính xác,
tiếp theo sử dụng lệnh grep để trích xuất dữ  liệu  cần tìm. Theo dữ  liệu  được  cung  cấp password  nằm cạnh từ millionth
    
        grep  millionth  data.txt
 > Flag: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

### Level 8
Truy  cập  level  8

     sshpass  -p  'cvX2JJa4CFALtqS87jk27qwqGhBM9plV' ssh bandit8@bandit.labs.overthewire.org -p 2220      

Password  cho level tiếp theo vẫn là được lưu trong file data.txt  và pass là  dòng  text chỉ xuất hiện một lần. Nếu  chỉ  sử  dụng  lệnh cat không  thì thấy  có rất nhiều dòng text  sẽ  không  biết chính xác đâu là dòng  text cần  tìm. Vì  vậy  sao khi cat sử dụng piping để output của lệnh cat sẽ là  input của lệnh sort. Lênh  sort  sẽ  sắp  xếp  các  dòng  text  giống nhau  lại. Sau  đó  sử  dụng  thêm  lệnh  uniq với option  -u  để  có  thể  in  ra  dòng  text  chỉ  xuất hiện một lần.

        cat  data.txt  | sort  | uniq  -u
> Flagg: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

### Level 9
Truy  cập level 9 bằng  câu  lệnh  

      sshpass  -p 'UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR' ssh bandit9@bandit.labs.overthewire.org -p 2220
      
Password  cho  level  tiếp  theo  được  lưu  trong  data.txt, password  là  một  chuối  ký  tự  đọc  được  và  trước  nó  là  các ký  tự  '='. Để hiển thị  chuỗi  ký  tự  trong file  có thể sử dụng lệnh strings và với dữ  kiện là  trước  password  là  các  ký  tự  '=' sử  dụng  thêm  lệnh  grep  để  tìm  đúng password
        
        strings  data.txt  | grep  '=='
 >Flag: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
 
### Level 10
Truy  cập  vào  level  10

      sshpass  -p 'truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk' ssh bandit10@bandit.labs.overthewire.org -p 2220

Password cho  level tiếp theo được lưu trong  file data.txt  và  được  mã  hoá  base64. Để giải  mã  sử  dụng  câu lệnh.
       
       base64 -e  data.txt
> Flag: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
      
### Level 11
Truy  cập  vào  level  11 bằng  câu lệnh 

      sshpass  -p  'IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR' ssh bandit11@bandit.labs.overthewire.org -p 2220      
Password  được lưu trong file dataa.txt, các  ký  tự  được  rotated by 13 positions(ROT13). Sau  khi cat file data.txt  được  chuỗi  ký  tự  như  sau: 'Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'. Sử  dụng  ROT13 để  giải  mã  thu được password
> Flag: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

### Level 12
Truy cập vào level 12

      sshpass -p '5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu' ssh bandit12@bandit.labs.overthewire.org -p 2220  
Password ở level tiếp theo được lưu trong file data.txt, hexdump của file đã được nén lại nhiều lần. Trong level này mình được tạo thư mục trong /tmp bằng câu lệnh mkdir. Sau đó copy file data.txt và thư mục vừa tạo trong /tmp. Đầu tiên chuyển file data.txt sang file binary
       
       xxd -r data.txt > file.bin
      
> Flag: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

### Level 13
Truy  cập vào level 13 bằng câu lệnh 

        sshpass -p '8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL' ssh bandit13@bandit.labs.overthewire.org -p 2220
Password được lưu trong /etc/bandit_pass/bandit14, file bandit14 chỉ có user bandit14 được đọc. Trong level này mình được cung cấp một private ssh key để truy cập bandit14.
        
        ssh bandit14@localhost -i sshkey.private 
 Sau đó sử dụng lệnh cat để nhận password 
  
        cat /etc/bandit_pass/bandit14
> Flag: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

### Level 14
Truy  cập vào level 14 bằng câu lệnh 

        sshpass -p '4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e' ssh bandit14@bandit.labs.overthewire.org -p 2220
Để nhận được password cho level tiếp theo bằng cách gửi password hiện tại đến localhost ở port 30000
        
        echo '4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e' | nc localhost 30000

> Flag: BfMYroe26WYalil77FoDi9qh59eK5xNr

### Level 15
Truy  cập vào level 15 bằng câu lệnh 

        sshpass -p 'BfMYroe26WYalil77FoDi9qh59eK5xNr' ssh bandit15@bandit.labs.overthewire.org -p 2220
 
 Password cho level tiếp theo lấy được bằng cách gửi pass hiện tại đến localhost port 30001 sử dụng mã hóa ssl. Sử dụng openssl để kết nối
        
        openssl s_client -connect localhost:30001
 Sau khi connect vào chỉ cần nhâp password level hiện tại sẽ nhận được pass cho level tiếp theo
> Flag: cluFn7wTiGryunymYOu4RcffSxQluehd

### Level 16
Truy  cập vào level 16 bằng câu lệnh 

        sshpass -p 'cluFn7wTiGryunymYOu4RcffSxQluehd' ssh bandit16@bandit.labs.overthewire.org -p 2220
Password cho level tiếp theo lấy được bằng cách gửi password của level hiện tại đến cổng máy chủ localhost trên phạm vi 31000 - 32000. Việc đầu tiên là sử dụng nmap để scan port nào đang listen trên phạm vi này 
        
        nmap localhost -p 31000-32000
nmap scan 5 port đang open là 31046, 31518, 31691, 31790, 31960. Việc tiếp theo là gửi password đến 5 port này sử dụng openssl 
    
       cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31046
       cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31518
       cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31691
       cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31790
       cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31960
       
Ở port 31790 sẽ phản hồi lại một RSA private key. Tạo một file key trong /tmm/.key. Sau đó cấp quyền cho nó
        
        cd /tmp
        vim .key
        chmod 700 .key
Sử dụng file .key này đăng nhập bandit17 

        ssh bandit17@localhost -i .key
Cuối cùng sử dụng cat lấy password cho level tiếp theo

        cat /etc/bandit_pass/bandit17
> Flag: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

### Level 17
Truy  cập vào level 17 bằng câu lệnh 

        sshpass -p 'xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn' ssh bandit17@bandit.labs.overthewire.org -p 2220
 Trong level này có hai file passwords.old và passwords.new. Pass cho level tiếp theo này trong file password.new. Trong passwords.new có một dòng bị thay đổi. Để tìm được dòng khác này sử dụng lệnh diff
    
        diff passwords.old passwords.new
> Flag: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
### Level 18
Truy cập level 18 bằng ssh, password cho level tiếp theo lưu trong file readme 

        sshpass -p 'kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd' ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
   
> Flag: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

### Level 19
        ssh bandit19@bandit.labs.overthewire.org -p 2220
        ls -al
        ./bandit20-do
        ./bandit20-do id
        ./bandit20-do cat /etc/bandit_pass/bandi20
![level 19](https://user-images.githubusercontent.com/83420725/134473841-6245dbe9-951e-4c6a-847e-72b4f4ede700.png)
> Flag: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

### Level 20
![Screen Shot 2021-09-23 at 3 37 52 PM](https://user-images.githubusercontent.com/83420725/134477665-d66cbcdf-4e19-4156-893e-6764fde835de.png)
![Screen Shot 2021-09-23 at 3 38 04 PM](https://user-images.githubusercontent.com/83420725/134477674-3ddd80bc-33f5-4817-adf7-82dca80903ad.png)
> Flag: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr


### Level 21 
          ssh bandit21@bandit.labs.overthewire.org -p 2220
          cd  /etc/cron.d/
          ls -al
          cat cronjob_bandit22
          cat /usr/bin/cronjob_bandit22.sh
          cd /tmp && cat t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
![level21](https://user-images.githubusercontent.com/83420725/134500523-a0b10e89-c2c9-452f-b50d-6bf3be39e958.png)
> Flag: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

### Level 22
           ssh bandit22@bandit.labs.overthewire.org -p 2220
           ls -l /etc/cron.d/
           cat /etc/cron.d/cronjob_bandit23
           cat /usr/bin/cronjob_bandit23.sh
           myname='bandit23'
           echo I am user $myname | md5sum | cut -d ' ' -f 1
           cat /tmp/8ca319486bfbbc3663ea0fbe81326349
![level22](https://user-images.githubusercontent.com/83420725/134503313-159334a4-26a4-46e9-9a7f-8855ac9db40e.png)
> Flag: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

### Level 23
           sshpass -p 'jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n' ssh bandit23@bandit.labs.overthewire.org -p 2220
> Flag: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

### Level 24


