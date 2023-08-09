#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle
 *@list: a pointer to the head
 *Return: 0 if there is no cycle 1 if they is
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	while (hare && tortoise->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1);
		}
	}
		return (0);
}
