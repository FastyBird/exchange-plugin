<?php declare(strict_types = 1);

/**
 * BeforeMessagePublished.php
 *
 * @license        More in LICENSE.md
 * @copyright      https://www.fastybird.com
 * @author         Adam Kadlec <adam.kadlec@fastybird.com>
 * @package        FastyBird:Exchange!
 * @subpackage     Events
 * @since          1.0.0
 *
 * @date           19.06.22
 */

namespace FastyBird\Core\Exchange\Events;

use FastyBird\Core\Application\Documents as ApplicationDocuments;
use FastyBird\Library\Metadata\Types as MetadataTypes;
use Symfony\Contracts\EventDispatcher;

/**
 * Before message published event
 *
 * @package        FastyBird:Exchange!
 * @subpackage     Events
 *
 * @author         Adam Kadlec <adam.kadlec@fastybird.com>
 */
class BeforeMessagePublished extends EventDispatcher\Event
{

	public function __construct(
		private readonly MetadataTypes\Sources\Source $source,
		private readonly string $routingKey,
		private readonly ApplicationDocuments\Document|null $entity,
	)
	{
	}

	public function getSource(): MetadataTypes\Sources\Source
	{
		return $this->source;
	}

	public function getRoutingKey(): string
	{
		return $this->routingKey;
	}

	public function getEntity(): ApplicationDocuments\Document|null
	{
		return $this->entity;
	}

}
