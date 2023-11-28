#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle
 * @list: Linked list to be checked
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *low = list;
	listint_t *high = list;

	if (!list)
		return (0);

	for (; low && high && high->next; low = low->next, high = high->next->next)
	{
		if (low == high)
			return (1);
	}

	return (0);
}
