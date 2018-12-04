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

	if (list == NULL || end == NULL)
		return (0);
	while (end)
	{
		end = end->next;
		end = end->next;
		if (end == list)
			return (1);
		list = list->next;
	}
	return (0);
}
