#include "lists.h"
#include <stddef.h>
/**
 *is_palindrome - checks if a number is a palindrome
 *@head: pointer to the head of the list
 *Return:1 if the list is a palindrome
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *next = NULL;
	int num_pal = 1;

		if(*head == NULL)
			return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast != NULL)
		slow = slow->next;
	while (prev != NULL)
	{
		if (prev->n != slow->n)
			num_pal = 0;
		next = prev->next;
		prev->next = slow;
		slow = prev;
		prev = next;
	}
	return (num_pal);
}
