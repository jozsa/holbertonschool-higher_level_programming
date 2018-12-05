#include "lists.h"

/**
 * check_cycle - Checks a singly linked lists for a cycle
 * @list: The list to be checked
 *
 * Return: 1 if there is a cycle, 0 if none
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list;
	slow = list;

	if (fast == NULL || slow == NULL)
		return (0);
	while (fast && (fast = fast->next))
	{
		if (fast == slow)
			return (1);
		fast = fast->next;
		if (fast == slow)
			return (1);
		slow = slow->next;
	}
	return (0);
}
