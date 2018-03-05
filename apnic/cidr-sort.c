#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long ip2num(char *cidr)
{
  char *p;
  char ip_str[1024];
  unsigned long ip = 0;
  unsigned long mul = 256*256*256;

  strcpy(ip_str, cidr);
  p = strtok(ip_str, "/");
  if (p == NULL) return 0;
  // printf("Convert IP: %s\n", p);
  p = strtok(p, ".");
  if (p == NULL) return 0;
  ip += (unsigned long)(atoi(p)) * mul;
  while (p = strtok(NULL, ".")) {
    mul = mul / 256;
    ip += (unsigned long)(atoi(p)) * mul;
  }
  return ip;
}

static int ip_cmp(const void *p1, const void *p2)
{
  unsigned long ip1, ip2;

  if (p1 == NULL && p2 == NULL) return 0;
  if (p1 == NULL) return 1;
  if (p2 == NULL) return -1;
  ip1 = ip2num((char *)p1);
  ip2 = ip2num((char *)p2);

  if (ip1 > ip2) return 1;
  else if (ip1 < ip2) return -1;
  else return 0;
}

int main(int argc, char *argv[])
{
  char buf[1024];
  char cidr[10240][1024];
  char *p;
  int i = 0, len;

  while (gets(buf)) {
    // printf("%s\n",buf);
/*
    p = malloc(strlen(buf)+1);
    strcpy(p, buf);
    cidr[i] = p;
*/
    strcpy(&cidr[i][0], buf);
    i++;
  }
  len = i;
  qsort(&cidr[0],len,1024*sizeof(char),ip_cmp);
  for (i = 0; i < len; i++) {
    printf("%s\n", cidr[i]);
  }
  // printf("Cmp Count: %d, len: %d\n", cnt, len);
}
