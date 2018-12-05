#include "lists.h"

/**
 * insert_node - Insert a node into a sorted singly linked list
 * @head: A pointer to the singly linked list
 * @number: The new node's number
 *
 * Return: Pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;
	listint_t *last = *head;
	int count = 0, index = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL || *head == NULL)
		return (NULL);
	new->n = number;
	while (new->n > current->n && current->next != NULL)
	{
		current = current->next;
		count++;
	}
	while (last->next != NULL)
		last = last->next;
	if (new->n > last->n)
	{
		new->next = NULL;
		last->next = new;
	}
	else if (count == 0)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		current = *head;
		for (index = 0; index < (count - 1); index++)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
