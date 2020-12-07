#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Entry Point
 * Description: Check if signly linked list has cycle in it
 * @list: pointer to head of list
 * Return: 1 for true, 0 for false
 */

int check_cycle(listint_t *list)
{
  listint_t *slow = list;
  listint_t *fast = list;
  
  while (fast != NULL && fast->next != NULL)
    {
      slow = slow->next;          
      fast = fast->next->next;      
  
      if (slow == fast)  
	return (1);
    }
  return (0);  
}
