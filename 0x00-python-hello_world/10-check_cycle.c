#include "lists.h"

/**
 * check_cycle - Checks a singly linked lists for a cycle
 * @list: The list to be checked
 *
 * Return: 1 if there is a cycle, 0 if none
 */

int check_cycle(listint_t *list)
{
	listint_t *end;

	end = list;

	if (end == NULL)
		return (0);
	while (end)
	{
		if (end->next == NULL)
			return (0);
		if (end->next == list)
			return (1);
		end = end->next;
	}
	return (0);
}
